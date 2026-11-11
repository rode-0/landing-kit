const assert = require('assert');
const { lpkStatus, lpkClock } = require('../claude/library/behaviors.js');
const cfg = { tz: 'America/New_York',
  hours: { mon: [], tue: [], wed: [['07:00','14:00']], thu: [['07:00','14:00']], fri: [['07:00','14:00']], sat: [['07:00','14:00']], sun: [['07:00','14:00']] },
  closed: { '2026-11-26': 'Thanksgiving', '2026-11-27': 'Thanksgiving' },
  words: { open: 'Open now until {close}', soon: 'Opens at {open} today', closed: 'Closed now. Back {day} at {open}', holiday: 'Closed today for {why}. Back {day} at {open}' } };
const at = s => new Date(s);
assert.strictEqual(lpkClock('07:00'), '7am'); assert.strictEqual(lpkClock('17:30'), '5:30pm'); assert.strictEqual(lpkClock('12:00'), '12pm'); assert.strictEqual(lpkClock('00:00'), '12am');
// Wed 2026-11-18 09:00 ET = 14:00Z
assert.strictEqual(lpkStatus(at('2026-11-18T14:00:00Z'), cfg).text, 'Open now until 2pm');
// Wed 06:00 ET
assert.strictEqual(lpkStatus(at('2026-11-18T11:00:00Z'), cfg).text, 'Opens at 7am today');
// Wed 15:00 ET -> tomorrow
assert.strictEqual(lpkStatus(at('2026-11-18T20:00:00Z'), cfg).text, 'Closed now. Back tomorrow at 7am');
// Sun 15:00 ET -> Mon,Tue closed -> Wednesday
assert.strictEqual(lpkStatus(at('2026-11-22T20:00:00Z'), cfg).text, 'Closed now. Back Wednesday at 7am');
// Thanksgiving Thu 10:00 ET -> holiday, back Saturday
assert.strictEqual(lpkStatus(at('2026-11-26T15:00:00Z'), cfg).text, 'Closed today for Thanksgiving. Back Saturday at 7am');
// Wed 25th after close -> Thu/Fri closed -> Saturday
assert.strictEqual(lpkStatus(at('2026-11-25T20:00:00Z'), cfg).text, 'Closed now. Back Saturday at 7am');
// late night UTC rollover: Wed 23:30 ET = Thu 04:30Z
assert.strictEqual(lpkStatus(at('2026-11-19T04:30:00Z'), cfg).text, 'Closed now. Back tomorrow at 7am');
// DST spring: Sun 2027-03-14 10:00 EDT = 14:00Z (open)
assert.strictEqual(lpkStatus(at('2027-03-14T14:00:00Z'), cfg).open, true);
// split hours + other tz
const c2 = { tz: 'America/Chicago', hours: { mon: [['07:00','12:00'],['13:00','19:00']], tue:[], wed:[], thu:[], fri:[], sat:[['08:00','12:00']], sun:[] }, words: cfg.words };
assert.strictEqual(lpkStatus(at('2026-11-16T18:30:00Z'), c2).text, 'Opens at 1pm today'); // Mon 12:30 CT
assert.strictEqual(lpkStatus(at('2026-11-16T20:00:00Z'), c2).text, 'Open now until 7pm');
console.log('behaviors: all tests passed');
// long closure: barber closed Sun-Mon + Thanksgiving week Tue 24 - Sat 28; Sat 2026-11-21 after close (3pm MT) -> Tuesday, Dec 1
const { lpkNextClass } = require('../claude/library/behaviors.js');
const b = { tz: 'America/Boise', hours: { sun: [], mon: [], tue: [['09:00','19:00']], wed: [['09:00','19:00']], thu: [['09:00','19:00']], fri: [['09:00','19:00']], sat: [['08:00','15:00']] },
  closed: { '2026-11-24': 'Thanksgiving week', '2026-11-25': 'Thanksgiving week', '2026-11-26': 'Thanksgiving week', '2026-11-27': 'Thanksgiving week', '2026-11-28': 'Thanksgiving week' },
  words: { open: 'Open until {close}', closed: 'Closed now. Back {day} at {open}' } };
assert.strictEqual(lpkStatus(new Date('2026-11-21T23:00:00Z'), b).text, 'Closed now. Back Tuesday, Dec 1 at 9am');
const sch = { tz: 'America/Chicago', classes: [ {day:'mon',time:'06:15',name:'Gentle Flow'}, {day:'mon',time:'17:30',name:'Slow Flow'}, {day:'sat',time:'08:00',name:'Prenatal'} ] };
assert.strictEqual(lpkNextClass(new Date('2026-11-16T15:00:00Z'), sch), 'Next class: Slow Flow, today at 5:30pm'); // Mon 9am CT
assert.strictEqual(lpkNextClass(new Date('2026-11-17T01:00:00Z'), sch), 'Next class: Prenatal, Saturday at 8am');  // Mon 7pm CT
assert.strictEqual(lpkNextClass(new Date('2026-11-21T20:00:00Z'), sch), 'Next class: Gentle Flow, Monday at 6:15am'); // Sat 2pm CT
console.log('long closure + next class: passed');
