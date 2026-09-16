# Design verification plan - SC-A0 / M1

| ID | Requirement / question | Method | Sample / proposed acceptance | Evidence / disposition |
|---|---|---|---|---|
| DV-01 | Frame and fixture datum repeatability | measure fixture artifact after installation/removal | 30 cycles; target <=0.10 mm, proposed | raw measurements; revise if not met |
| DV-02 | Guide avoids terminal/housing damage | guided insertion plus microscope inspection | 30 inserts per guide variant; zero observed damage target | images, retained samples, NCRs |
| DV-03 | Force path detects excessive resistance | calibrated load + inserted fault simulation | 10 controlled fault trials; detect all in test set | trace data, threshold rationale |
| DV-04 | Seating indicator is not a false mechanical claim | compare trace/datum with approved inspection/retention method | sample size determined by responsible engineer | correlation record; no pass until established |
| DV-05 | Electrical mapping detects opens/mis-map/shorts | calibrated mating/far-end fixture with fault coupons | >=10 of each controlled fault class | matrix report, uncertainty notes |
| DV-06 | Guard/E-stop/power recovery safe behavior | qualified test procedure | each M1 configuration after change | signed safety test record |
| DV-07 | Camera/light visibility | target and representative connector samples | all four cavities, representative terminal finish | exposure/glare record |
| DV-08 | Service/assembly access | timed supervised assembly/service review | M1-001 and M1-002 | access findings and design actions |
| DV-09 | Recipe/controller command boundaries | automated tests and protocol review | every release | test report; raw motion remains rejected |

Acceptance values above are proposed engineering targets, not demonstrated limits. A qualified reviewer must approve methods, sample sizes, and final criteria for intended use.
