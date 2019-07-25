## Known user
* greet
  - action_check_profile
  - slot{"user_exists": "true"}
  - slot{"user_name": "Matthew"}
  - slot{"measure_user": "true"}
  - utter_greet

## Known user II
* start
  - action_check_profile
  - slot{"user_exists": "true"}
  - slot{"user_name": "Matthew"}
  - slot{"measure_user": "true"}
  - utter_greet

## Unknown user
* greet
  - action_check_profile
  - slot{"user_exists": "false"}
  - utter_unknown

## Unknown user II
* start
  - action_check_profile
  - slot{"user_exists": "false"}
  - utter_unknown

## say goodbye
* goodbye
  - utter_goodbye

## basic new table
* new_table
  - action_check_profile
  - slot{"user_exists": "true"}
  - slot{"user_name": "Matthew"}
  - slot{"user_gender": "male"}
  - slot{"measure_user": "true"}
  - utter_give_new_table


## basic start training
* start_training
  - action_check_profile
  - slot{"user_exists": "true"}
  - slot{"user_name": "Matthew"}
  - slot{"user_gender": "male"}
  - slot{"measure_user": "true"}
  - action_start_training

## Training False
* start_training
    - action_check_profile
    - slot{"user_exists": false}
    - utter_unknown

## Get Complete Measurements True
* get_measurements
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Matthew"}
    - slot{"user_gender": "male"}
    - slot{"measure_user": "true"}
    - measurement_form
    - form{"name": "measurement_form"}
    - form{"name": null}


## Get Basic Measurements False
* get_measurements
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Matthew"}
    - slot{"measure_user": "false"}
    - utter_no_measurements_selected

## New user Happy Path
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "Matthew"}
    - slot{"PERSON":"Matthew"}
    - action_set_name
    - slot{"user_name":"Matthew"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* confirm_birthdate{"time":"26-6-1995"}
    - action_set_birthdate
    - slot{"birthdate":"26-6-1995"}
    - utter_training_type
* training_confirmation {"training_type": "Muscle toning"}
    - slot{"training_type": "Muscle toning"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* affirm
    - action_confirm_user_wants_routine
    - slot{"wants_routine": "true"}
    - utter_reminder_routine
    - utter_do_you_want_diets
* affirm
    - action_confirm_user_wants_diets
    - slot{"wants_diets": "true"}
    - utter_confirm_diets
    - utter_track_progress
* affirm
    - action_confirm_user_wants_measurements
    - slot{"measure_user": "true"}
    - action_add_user
    - slot{"user_id": "1"}
    - utter_ask_measure_now
* affirm
    - utter_ask_eaten
* deny
    - measurement_form
    - form{"name": "measurement_form"}
    - form{"name": null}
    - utter_welcome

## New user Happy Path II
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "Matthew"}
    - slot{"PERSON":"Matthew"}
    - action_set_name
    - slot{"user_name":"Matthew"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* confirm_birthdate{"time":"26-6-1995"}
    - action_set_birthdate
    - slot{"birthdate":"26-6-1995"}
    - utter_training_type
* training_confirmation {"training_type": "Muscle toning"}
    - slot{"training_type": "Muscle toning"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* deny
    - utter_do_you_want_diets
* deny
    - utter_track_progress
* affirm
    - action_confirm_user_wants_measurements
    - slot{"measure_user": "true"}
    - action_add_user
    - slot{"user_id": "1"}
    - utter_ask_measure_now
* affirm
    - utter_ask_eaten
* affirm
    - utter_reminder_measurement
* measurement_reminder{"measurement_hour": "8:00"}
    - slot{"measurement_hour": "8:00"}
    - utter_welcome

## New User Happy Path III
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "Matthew"}
    - slot{"PERSON": "Matthew"}
    - action_set_name
    - slot{"user_name": "Matthew"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* confirm_birthdate{"number": "1995", "time": "1995-06-26T00:00:00.000+02:00"}
    - slot{"number": "1995"}
    - slot{"time": "1995-06-26T00:00:00.000+02:00"}
    - action_set_birthdate
    - slot{"birthdate": "1995-06-26"}
    - utter_training_type
* training_confirmation{"training_type": "Muscle toning"}
    - slot{"training_type": "Muscle toning"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* affirm
    - action_confirm_user_wants_routine
    - slot{"wants_routine": "true"}
    - utter_reminder_routine
    - utter_do_you_want_diets
* affirm
    - action_confirm_user_wants_diets
    - slot{"wants_diets": "true"}
    - utter_confirm_diets
    - utter_track_progress
* deny
    - action_add_user
    - slot{"user_id": "1"}
    - utter_welcome

## New User Happy Path .1
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "pablo", "GPE": "Pablo"}
    - slot{"PERSON": "pablo"}
    - action_set_name
    - slot{"user_name": "pablo"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* confirm_birthdate{"DATE": "June 26 1995", "time": "1995-06-26T00:00:00.000+02:00", "number": "1995"}
    - slot{"number": "1995"}
    - slot{"time": "1995-06-26T00:00:00.000+02:00"}
    - action_set_birthdate
    - slot{"birthdate": "1995-06-26"}
    - utter_training_type
* training_confirmation{"training_type": "volume"}
    - slot{"training_type": "volume"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* affirm
    - action_confirm_user_wants_routine
    - slot{"wants_routine": "true"}
    - utter_reminder_routine
    - utter_do_you_want_diets
* affirm
    - action_confirm_user_wants_diets
    - slot{"wants_diets": "true"}
    - utter_confirm_diets
    - utter_track_progress
* affirm
    - action_confirm_user_wants_measurements
    - slot{"measure_user": "true"}
    - action_add_user
    - slot{"user_id": "1"}
    - utter_ask_measure_now
* affirm
    - utter_ask_eaten
* deny
    - measurement_form
    - form{"name": "measurement_form"}
    - slot{"requested_slot": "weight"}
* form: add_weight{"number": "80", "QUANTITY": "80 kg"}
    - slot{"number": "80"}
    - form: measurement_form
    - slot{"weight": "80"}
    - slot{"requested_slot": "bodyfatratio"}
* form: add_bodyfatratio{"number": 19, "PERCENT": "19%"}
    - slot{"number": 19}
    - form: measurement_form
    - slot{"bodyfatratio": "19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_welcome

## Don't want to join
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_gender": null}
    - utter_unknown
* deny
    - utter_not_interested

## Generated Story -5969015667142631679
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "Matt"}
    - slot{"PERSON": "Matt"}
    - action_set_name
    - slot{"user_name": "Matt"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* start_training{"DATE": "1995-06-26", "time": "1995-06-26T00:00:00.000+02:00"}
    - slot{"time": "1995-06-26T00:00:00.000+02:00"}
    - action_set_birthdate
    - slot{"birthdate": "1995-06-26"}
    - utter_training_type
* training_confirmation{"training_type": "volume"}
    - slot{"training_type": "volume"}
    - utter_reinforce_objective
    - undo
    - utter_do_you_want_routine
* affirm
    - action_confirm_user_wants_routine
    - slot{"wants_routine": true}
    - utter_reminder_routine
    - utter_do_you_want_diets
* affirm
    - action_confirm_user_wants_diets
    - slot{"wants_diets": true}
    - utter_confirm_diets
    - utter_track_progress
* affirm
    - action_confirm_user_wants_measurements
    - slot{"measure_user": true}
    - action_add_user
    - slot{"user_id": "1"}
    - utter_ask_measure_now
* affirm{"time": "2019-07-25T13:26:24.000+02:00"}
    - slot{"time": "2019-07-25T13:26:24.000+02:00"}
    - utter_ask_eaten
* deny
    - measurement_form
    - form{"name": "measurement_form"}
    - slot{"requested_slot": "weight"}
* form: add_weight{"number": "83", "QUANTITY": "83 kg"}
    - slot{"number": "83"}
    - form: measurement_form
    - slot{"weight": "83"}
    - slot{"requested_slot": "bodyfatratio"}
* form: add_bodyfatratio{"number": "19", "PERCENT": "19 %"}
    - slot{"number": "19"}
    - form: measurement_form
    - slot{"bodyfatratio": ["19", "19"]}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_welcome

## Generated Story 3889498053636154162
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* greet{"PERSON": "Jennifer"}
    - slot{"PERSON": "Jennifer"}
    - action_set_name
    - slot{"user_name": "Jennifer"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "female"}
    - slot{"user_gender": "female"}
    - utter_birthdate
* confirm_birthdate{"DATE": "August 29 1876", "time": "1876-08-29T00:00:00.000-00:15"}
    - slot{"time": "1876-08-29T00:00:00.000-00:15"}
    - action_set_birthdate
    - slot{"birthdate": "1876-08-29"}
    - utter_training_type
* training_confirmation{"training_type": "definition"}
    - slot{"training_type": "definition"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* affirm
    - action_confirm_user_wants_routine
    - slot{"wants_routine": true}
    - utter_reminder_routine
    - utter_do_you_want_diets
* affirm
    - action_confirm_user_wants_diets
    - slot{"wants_diets": true}
    - utter_confirm_diets
    - utter_track_progress
* affirm
    - action_confirm_user_wants_measurements
    - slot{"measure_user": true}
    - action_add_user
    - slot{"user_id": "1"}
    - utter_ask_measure_now
* deny
    - utter_welcome

## Generated Story 2892106610303573279
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* greet{"PERSON": "Jesus"}
    - slot{"PERSON": "Jesus"}
    - action_set_name
    - slot{"user_name": "Jesus"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* confirm_birthdate{"DATE": "February 12 1975", "time": "1975-02-12T00:00:00.000+01:00"}
    - slot{"time": "1975-02-12T00:00:00.000+01:00"}
    - action_set_birthdate
    - slot{"birthdate": "1975-02-12"}
    - utter_training_type
* get_measurements{"training_type": "weight_loss"}
    - slot{"training_type": "weight_loss"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* affirm
    - action_confirm_user_wants_routine
    - slot{"wants_routine": true}
    - utter_reminder_routine
    - utter_do_you_want_diets
* deny
    - action_confirm_user_wants_diets
    - slot{"wants_diets": true}
    - utter_track_progress
* deny
    - action_add_user
    - slot{"user_id": "1"}
    - utter_welcome

## Generated Story 100149762851612025
* start
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"ORG": "Felipe"}
    - rewind
* name_confirmation{"PERSON": "Felipe"}
    - slot{"PERSON": "Felipe"}
    - action_set_name
    - slot{"user_name": "Felipe"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* confirm_birthdate{"time": "1979-09-01T00:00:00.000+02:00", "DATE": "September 1 1979"}
    - slot{"time": "1979-09-01T00:00:00.000+02:00"}
    - action_set_birthdate
    - slot{"birthdate": "1979-09-01"}
    - utter_training_type
* training_confirmation{"training_type": "volume"}
    - slot{"training_type": "volume"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* deny
    - utter_do_you_want_diets
* affirm
    - utter_track_progress
* deny
    - action_add_user
    - slot{"user_id": "1"}
    - utter_welcome

## Generated Story -9031546320465577542
* start
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "Maria"}
    - slot{"PERSON": "Maria"}
    - action_set_name
    - slot{"user_name": "Maria"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* confirm_birthdate{"time": "1993-06-21T00:00:00.000+02:00", "DATE": "June 21 1993"}
    - slot{"time": "1993-06-21T00:00:00.000+02:00"}
    - action_set_birthdate
    - slot{"birthdate": "1993-06-21"}
    - utter_training_type
* training_confirmation{"training_type": "definition"}
    - slot{"training_type": "definition"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* deny
    - utter_do_you_want_diets
* deny
    - utter_track_progress
* affirm
    - action_confirm_user_wants_measurements
    - slot{"measure_user": true}
    - action_add_user
    - slot{"user_id": "1"}
    - utter_ask_measure_now
* affirm
    - utter_ask_eaten
* deny
    - measurement_form
    - form{"name": "measurement_form"}
    - slot{"requested_slot": "weight"}
* form: add_weight{"number": "84", "QUANTITY": "84 kg"}
    - slot{"number": "84"}
    - form: measurement_form
    - slot{"weight": "84"}
    - slot{"requested_slot": "bodyfatratio"}
* form: confirm_birthdate{"number": 12, "PERCENT": "12 %"}
    - slot{"number": 12}
    - form: rewind
* form: add_bodyfatratio{"number": "12", "PERCENT": "12 %"}
    - slot{"number": "12"}
    - form: measurement_form
    - slot{"bodyfatratio": "12"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_welcome
