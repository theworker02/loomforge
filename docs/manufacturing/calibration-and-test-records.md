# Calibration and test record set — M1

**Document:** LF-MET-001 · **Revision:** A0 (proposed)

## Calibration record minimum fields

| Asset / record | Required fields | Failed/expired response |
|---|---|---|
| Force path | asset ID, sensor/conditioner P/N, mounting configuration, zero, known loads, method, date, operator, next review date, raw readings | remove from pass disposition; investigate overload/mounting change |
| Fixture datum | fixture ID, locator condition, artifact ID, coordinate results, repeatability cycles, ambient condition, operator | hold fixture and re-establish datum |
| Tray pickup map | tray ID, slot coordinates/orientation condition, measurement method, recipe compatibility | block affected recipes |
| Camera/vision lighting | camera/lens/light IDs, exposure/gain, work distance, target image references, ambient-light condition | rerun documented setup; do not compare uncontrolled images |
| Electrical fixture | fixture ID, test plug P/N/lot, reference-path result, lead/switch configuration, test voltage/current limits | mark test unavailable; do not report pass |

## Electrical test record minimum fields

| Field | Record |
|---|---|
| Job / unit / fixture / recipe identifiers |  |
| Test voltage and current limits |  |
| Reference/self-test result before and after run |  |
| Expected pin map |  |
| Measured map / opens / shorts / ambiguous points |  |
| Instrument and switching-path identifiers |  |
| Lead/contact/switching-resistance limitation statement |  |
| Operator / timestamp / raw-result location |  |

The mapping fixture may establish the defined connection map under a controlled test method. It does not alone establish terminal retention or a precision contact-resistance value.
