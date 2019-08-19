## Known user
* greet
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Matthew"}
    - slot{"measure_user": true}
    - slot{"user_gender": "male"}
    - slot{"user_id": "1"}
    - utter_greet

## Known user
* user_wants_to_join
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Matthew"}
    - slot{"measure_user": true}
    - slot{"user_gender": "male"}
    - slot{"user_id": "1"}
    - utter_already_in

## New user asks again to join
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_id": "0"}
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
* confirm_birthdate{"DATE": "1995-06-26", "time": "1995-06-26T00:00:00.000+02:00"}
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
* affirm
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
* user_wants_to_join
  - utter_already_in

## Known user
* greet
  - action_check_profile
  - slot{"user_exists": true}
  - slot{"user_name": "Matthew"}
  - slot{"measure_user": false}
  - slot{"user_gender": "male"}
  - slot{"user_id": "1"}
  - utter_greet
* get_measurements
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
  - utter_measurements_taken

## Known user II
* start
  - action_check_profile
  - slot{"user_exists": true}
  - slot{"user_name": "Matthew"}
  - slot{"measure_user": true}
  - slot{"user_gender": "male"}
  - slot{"user_id": "1"}
  - utter_greet

## Don't Understand Known
* chitchat
  - action_check_profile
  - slot{"user_exists": true}
  - slot{"user_name": "Matthew"}
  - slot{"measure_user": true}
  - slot{"user_gender": "male"}
  - slot{"user_id": "1"}
  - utter_dont_understand


## Random deny
* deny
  - action_check_profile
  - slot{"user_exists": true}
  - slot{"user_name": "Matthew"}
  - slot{"measure_user": true}
  - slot{"user_gender": "male"}
  - slot{"user_id": "1"}
  - utter_dont_understand

## Random deny Unknown
* deny
  - slot{"user_exists": false}
  - slot{"user_name": null}
  - slot{"measure_user": null}
  - slot{"user_id": "0"}
  - slot{"user_gender": null}
  - utter_dont_understand
  - utter_unknown

## Random affirm
* affirm
  - action_check_profile
  - slot{"user_exists": true}
  - slot{"user_name": "Matthew"}
  - slot{"measure_user": true}
  - slot{"user_gender": "male"}
  - slot{"user_id": "1"}
  - utter_dont_understand

## Random affirm Unknown
* affirm
  - slot{"user_exists": false}
  - slot{"user_name": null}
  - slot{"measure_user": null}
  - slot{"user_id": "0"}
  - slot{"user_gender": null}
  - utter_dont_understand
  - utter_unknown

## Unknown user
* greet
  - action_check_profile
  - slot{"user_exists": "false"}
  - utter_unknown

## Dont understand
* start
  - action_check_profile
  - slot{"user_exists": "false"}
  - utter_unknown

## Unknown user II
* chitchat
  - action_check_profile
  - slot{"user_exists": "false"}
  - utter_dont_understand

## say goodbye
* goodbye
  - utter_goodbye

## Help
* help
  - action_check_profile
  - slot{"user_exists": true}
  - slot{"user_name": "Matthew"}
  - slot{"user_gender": "male"}
  - slot{"measure_user": true}
  - slot{"user_id": "1"}
  - utter_give_help

## Help Unknown
* help
  - action_check_profile
  - slot{"user_exists": "false"}
  - utter_give_help
  - utter_unknown

## basic new table
* new_table{"table_type": "exercise"}
  - slot{"table_type": "exercise"}
  - action_check_profile
  - slot{"user_exists": true}
  - slot{"user_name": "Matthew"}
  - slot{"user_gender": "male"}
  - slot{"measure_user": true}
  - slot{"user_id": "1"}
  - utter_give_new_table
* thanks
  - utter_your_welcome

## weird new table
* new_table
  - action_check_profile
  - slot{"user_exists": true}
  - slot{"user_name": "Matthew"}
  - slot{"user_gender": "male"}
  - slot{"measure_user": true}
  - slot{"user_id": "1"}
  - utter_table_type
* chitchat
  - utter_do_you_want_to_continue
* affirm
  - utter_table_type
* confirm_table{"table_type": "diet"}
  - slot{"table_type":"diet"}
  - utter_give_new_table
* thanks
    - utter_your_welcome
* goodbye
    - utter_goodbye


## weird new table
* new_table
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Matthew"}
    - slot{"user_gender": "male"}
    - slot{"measure_user": true}
    - slot{"user_id": "1"}
    - utter_table_type
* chitchat
    - utter_do_you_want_to_continue
* deny
    - utter_ok

## New exercise table Unknown
* new_table{"table_type": "diet"}
    - slot{"table_type": "diet"}
    - action_check_profile
    - slot{"user_exists": "false"}
    - utter_unknown


## basic new diet table
* new_table{"table_type": "diet"}
    - slot{"table_type": "diet"}
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Matthew"}
    - slot{"user_gender": "male"}
    - slot{"measure_user": true}
    - slot{"user_id": "1"}
    - utter_give_new_table

## New diet table Unknown
* new_table{"table_type": "diet"}
    - slot{"table_type": "diet"}
    - action_check_profile
    - slot{"user_exists": "false"}
    - utter_unknown

## basic new table without filling the first slot
* new_table
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Matthew"}
    - slot{"user_gender": "male"}
    - slot{"measure_user": true}
    - slot{"user_id": "1"}
    - utter_table_type
* new_table{"table_type": "diet"}
    - slot{"table_type": "diet"}
    - utter_give_new_table

## New exercise table Unknown without slot
* new_table
    - action_check_profile
    - slot{"user_exists": "false"}
    - utter_unknown

##  show my progress
* show_my_progress
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Matthew"}
    - slot{"user_gender": "male"}
    - slot{"measure_user": true}
    - slot{"user_id": "1"}
    - action_show_progress

## show my progress Unknown
* show_my_progress
    - action_check_profile
    - slot{"user_exists": "false"}
    - utter_unknown

## basic start training
* start_training
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Matthew"}
    - slot{"user_gender": "male"}
    - slot{"measure_user": true}
    - slot{"user_id": "1"}
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
    - slot{"measure_user": true}
    - slot{"user_id": "1"}
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

    ## Generated Story 201719396436076367
    * greet
        - action_check_profile
        - slot{"user_exists": true}
        - slot{"user_name": "Test"}
        - slot{"measure_user": true}
        - slot{"user_gender": "male"}
        - slot{"user_id": "24"}
        - utter_greet
    * get_measurements
        - measurement_form
        - form{"name": "measurement_form"}
        - slot{"requested_slot": "weight"}
    * form: add_weight{"number": "84", "QUANTITY": "84 kg"}
        - slot{"number": "84"}
        - form: measurement_form
        - slot{"weight": "84"}
        - slot{"requested_slot": "bodyfatratio"}
    * form: add_bodyfatratio{"number": 16, "PERCENT": "16%"}
        - slot{"number": 16}
        - form: measurement_form
        - slot{"bodyfatratio": "16"}
        - slot{"weight": null}
        - slot{"bodyfatratio": null}
        - form{"name": null}
        - slot{"requested_slot": null}
        - utter_measurements_taken

## New user Happy Path
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_id": "0"}
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
    - slot{"time":"26-6-1995"}
    - action_set_birthdate
    - slot{"birthdate":"26-6-1995"}
    - utter_training_type
* training_confirmation {"training_type": "volume"}
    - slot{"training_type": "volume"}
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
* affirm
    - utter_ask_eaten
* deny
    - measurement_form
    - form{"name": "measurement_form"}
    - form{"name": null}
    - utter_measurements_taken
    - utter_welcome

## New user Happy Path II
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_id": "0"}
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
    - slot{"time":"26-6-1995"}
    - action_set_birthdate
    - slot{"birthdate":"26-6-1995"}
    - utter_training_type
* training_confirmation {"training_type": "volume"}
    - slot{"training_type": "volume"}
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
* affirm
    - utter_reminder_measurement
* measurement_reminder{"measurement_hour": "8:00"}
    - slot{"measurement_hour": "8:00"}
    - action_set_reminder
    - utter_welcome

## New User Happy Path III
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_id": "0"}
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
* training_confirmation{"training_type": "volume"}
    - slot{"training_type": "volume"}
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
    - slot{"user_id": "0"}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "pablo"}
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
    - utter_measurements_taken
    - utter_welcome

## Don't want to join
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_id": "0"}
    - slot{"user_gender": null}
    - utter_unknown
* deny
    - utter_not_interested

## New user 1
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_id": "0"}
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
* confirm_birthdate{"DATE": "1995-06-26", "time": "1995-06-26T00:00:00.000+02:00"}
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
* affirm
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
    - utter_measurements_taken
    - utter_welcome

## New user 2
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_id": "0"}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "Jennifer"}
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

## New User 3
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_id": "0"}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "Jesus"}
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
* training_confirmation{"training_type": "weight_loss"}
    - slot{"training_type": "weight_loss"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* affirm
    - action_confirm_user_wants_routine
    - slot{"wants_routine": true}
    - utter_reminder_routine
    - utter_do_you_want_diets
* deny
    - utter_track_progress
* deny
    - action_add_user
    - slot{"user_id": "1"}
    - utter_welcome
  * thanks
    - utter_your_welcome
  * goodbye
    - utter_goodbye

## Thanks
* thanks
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Test"}
    - slot{"measure_user": true}
    - slot{"user_gender": "male"}
    - slot{"user_id": "1"}
    - utter_your_welcome

## Thanks
* thanks
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Test"}
    - slot{"measure_user": true}
    - slot{"user_gender": "male"}
    - slot{"user_id": "1"}
    - utter_your_welcome
* goodbye
    - utter_goodbye

## Thanks
* thanks
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": 0}
    - utter_unknown



## New user 4
* start
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": null}
    - slot{"user_id": "0"}
    - slot{"user_gender": null}
    - utter_unknown
* affirm
    - utter_ask_name
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
    - action_confirm_user_wants_diets
    - slot{"wants_diets": true}
    - utter_confirm_diets
    - utter_track_progress
* deny
    - action_add_user
    - slot{"user_id": "1"}
    - utter_welcome

## New user 5
* start
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_id": "0"}
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
    - utter_measurements_taken
    - utter_welcome

## New user 6
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": null}
    - utter_unknown
* greet
    - utter_unknown
* greet
    - utter_unknown
* start_training
    - utter_unknown
* affirm
    - utter_ask_name
* chitchat
    - utter_do_you_want_to_continue
* affirm
    - utter_ask_name
* name_confirmation
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
* confirm_birthdate{"DATE": "Some day"}
    - utter_birthdate_correction
* confirm_birthdate{"time": "1999-03-23T00:00:00.000+01:00", "DATE": "March 23 1999"}
    - slot{"time": "1999-03-23T00:00:00.000+01:00"}
    - action_set_birthdate
    - slot{"birthdate": "1999-03-23"}
    - utter_training_type
* training_confirmation
    - utter_training_type
* training_confirmation{"training_type": "definition"}
    - slot{"training_type": "definition"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* chitchat
    - utter_do_you_want_routine
* affirm
    - action_confirm_user_wants_routine
    - slot{"wants_routine": true}
    - utter_reminder_routine
    - utter_do_you_want_diets
* deny
    - utter_do_you_want_to_continue
* affirm
    - utter_track_progress
* chitchat
    - utter_do_you_want_to_continue
* affirm
    - utter_track_progress
* affirm
    - action_confirm_user_wants_measurements
    - slot{"measure_user": true}
    - action_add_user
    - slot{"user_id": 7}
    - utter_ask_measure_now
* deny
    - utter_welcome

## Generated Story 4998284128767635694
* start_training
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": null}
    - utter_unknown
* greet
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "Raul"}
    - slot{"PERSON": "Raul"}
    - action_set_name
    - slot{"user_name": "Raul"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* chitchat
    - utter_do_you_want_to_continue
* affirm
    - utter_birthdate
* confirm_birthdate{"time": "1976-05-24T00:00:00.000+02:00", "DATE": "24 May 1976"}
    - slot{"time": "1976-05-24T00:00:00.000+02:00"}
    - action_set_birthdate
    - slot{"birthdate": "1976-05-24"}
    - utter_training_type
* chitchat
    - utter_do_you_want_to_continue
* affirm
    - utter_training_type
* training_confirmation{"training_type": "weight_loss"}
    - slot{"training_type": "weight_loss"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* greet
    - utter_do_you_want_to_continue
* affirm
    - utter_do_you_want_routine
* start_training
    - utter_do_you_want_to_continue
* affirm
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
* deny
    - action_add_user
    - slot{"user_id": "1"}
    - utter_welcome

## Generated Story 5542185230094879419
* greet{"PERSON": "Sam"}
    - slot{"PERSON": "Sam"}
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": null}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "matt"}
    - slot{"PERSON": "matt"}
    - action_set_name
    - slot{"user_name": "Matt"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* confirm_birthdate
    - utter_birthdate_correction
* confirm_birthdate{"DATE": "July 25 1946", "time": "1946-07-25T00:00:00.000+02:00"}
    - slot{"time": "1946-07-25T00:00:00.000+02:00"}
    - action_set_birthdate
    - slot{"birthdate": "1946-07-25"}
    - utter_training_type
* get_measurements
    - utter_do_you_want_to_continue
* affirm
    - utter_training_type
* training_confirmation{"training_type": "volume"}
    - slot{"training_type": "volume"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* help
    - utter_do_you_want_to_continue
* affirm
    - utter_do_you_want_routine
* deny
    - utter_do_you_want_diets
* affirm
    - action_confirm_user_wants_diets
    - slot{"wants_diets": true}
    - utter_confirm_diets
    - utter_track_progress
* chitchat
    - utter_do_you_want_to_continue
* affirm
    - utter_track_progress
* affirm
    - action_confirm_user_wants_measurements
    - slot{"measure_user": true}
    - action_add_user
    - slot{"user_id": 8}
    - utter_ask_measure_now
* deny
    - utter_welcome

## New table with confirmation
* greet
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Test"}
    - slot{"measure_user": true}
    - slot{"user_gender": "male"}
    - slot{"user_id": "1"}
    - utter_greet
* confirm_table{"table_type": "exercise"}
    - slot{"table_type": "exercise"}
    - utter_give_new_table
* new_table{"table_type": "diet"}
    - slot{"table_type": "diet"}
    - utter_give_new_table
* thanks
    - utter_welcome

## Generated Story 245669127735516757
* greet
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Test"}
    - slot{"measure_user": true}
    - slot{"user_gender": "male"}
    - slot{"user_id": "1"}
    - utter_greet
* new_table
    - utter_table_type
* new_table{"table_type": "diet"}
    - slot{"table_type": "diet"}
    - utter_give_new_table

## Generated Story -1133157421296206477
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": 0}
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
* confirm_birthdate{"DATE": "1997", "number": 1997}
    - slot{"number": 1997}
    - utter_birthdate_correction
* confirm_birthdate{"DATE": "23 November 1997", "time": "1997-11-23T00:00:00.000+01:00"}
    - slot{"time": "1997-11-23T00:00:00.000+01:00"}
    - action_set_birthdate
    - slot{"birthdate": "1997-11-23"}
    - utter_training_type
* training_confirmation{"training_type": "weight_loss"}
    - slot{"training_type": "weight_loss"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* affirm
    - action_confirm_user_wants_routine
    - slot{"wants_routine": true}
    - utter_reminder_routine
    - utter_do_you_want_diets
* deny
    - utter_track_progress
* deny
    - action_add_user
    - slot{"user_id": 10}
    - utter_welcome

## Generated Story 2497654792158485470
* user_wants_to_join
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": 0}
    - utter_ask_name
* name_confirmation{"PERSON": "maria"}
    - slot{"PERSON": "maria"}
    - action_set_name
    - slot{"user_name": "Maria"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* greet
    - utter_do_you_want_to_continue
* affirm
    - utter_birthdate
* confirm_birthdate{"time": "1995-06-26T00:00:00.000+02:00", "DATE": "June 26 1995"}
    - slot{"time": "1995-06-26T00:00:00.000+02:00"}
    - action_set_birthdate
    - slot{"birthdate": "1995-06-26"}
    - utter_training_type
* training_confirmation{"training_type": "volume"}
    - slot{"training_type": "volume"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* deny
    - utter_do_you_want_diets
* deny
    - utter_track_progress
* deny
    - action_add_user
    - slot{"user_id": 11}
    - utter_welcome

## Generated Story 1900581720888062920
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": 0}
    - utter_unknown
* deny
    - utter_not_interested
* affirm
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "Laura"}
    - slot{"PERSON": "Laura"}
    - action_set_name
    - slot{"user_name": "Laura"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "female"}
    - slot{"user_gender": "female"}
    - utter_birthdate
* confirm_birthdate{"time": "1995-06-01T00:00:00.000+02:00", "DATE": "june 1995"}
    - slot{"time": "1995-06-01T00:00:00.000+02:00"}
    - action_set_birthdate
    - slot{"birthdate": "1995-06-01"}
    - utter_training_type
* chitchat
    - utter_do_you_want_to_continue
* affirm
    - utter_training_type
* training_confirmation
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
    - utter_ask_measure_now
* affirm
    - utter_ask_eaten
* meal_eaten{"meal_eaten": "breakfast"}
    - utter_reminder_measurement
* measurement_reminder{"number": "8", "CARDINAL": "8", "time": "2019-07-30T08:00:00.000+02:00"}
    - slot{"number": "8"}
    - slot{"time": "2019-07-30T08:00:00.000+02:00"}
    - action_set_reminder
    - utter_welcome
* thanks
    - utter_your_welcome

## Generated Story 7592086091383127773
* help
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": 0}
    - utter_give_help
    - utter_unknown
* affirm
    - utter_ask_name
* get_measurements
    - utter_do_you_want_to_continue
* deny
    - utter_not_interested
* user_wants_to_join
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": 0}
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
* confirm_birthdate{"time": "1995-06-26T00:00:00.000+02:00", "DATE": "June 26 1995"}
    - slot{"time": "1995-06-26T00:00:00.000+02:00"}
    - action_set_birthdate
    - slot{"birthdate": "1995-06-26"}
    - utter_training_type
* user_wants_to_join
    - utter_do_you_want_to_continue
* affirm
    - utter_training_type
* training_confirmation{"training_type": "weight_loss"}
    - slot{"training_type": "weight_loss"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* greet
    - utter_do_you_want_to_continue
* affirm
    - utter_do_you_want_routine
* start_training
    - utter_do_you_want_to_continue
* affirm
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
* deny
    - action_add_user
    - slot{"user_id": "1"}
    - utter_welcome

## Generated Story 8414753653367125449
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": 0}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "matt"}
    - slot{"PERSON": "matt"}
    - action_set_name
    - slot{"user_name": "Matt"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* confirm_birthdate{"time": "2020-06-26T00:00:00.000+02:00", "DATE": "June 26"}
    - slot{"time": "2020-06-26T00:00:00.000+02:00"}
    - action_set_birthdate
    - utter_birthdate_correction
* confirm_birthdate{"time": "1995-06-26T00:00:00.000+02:00", "DATE": "June 26 1995"}
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
* affirm
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

## Generated Story 1164266183754180747
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": 0}
    - utter_unknown
* start{"ORG": "Ues"}
    - rewind
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
* confirm_birthdate{"DATE": "November 23", "time": "2019-11-23T00:00:00.000+01:00"}
    - slot{"time": "2019-11-23T00:00:00.000+01:00"}
    - action_set_birthdate
    - utter_birthdate_correction
* confirm_birthdate{"time": "1997-11-23T00:00:00.000+01:00", "DATE": "23 November 1997"}
    - slot{"time": "1997-11-23T00:00:00.000+01:00"}
    - action_set_birthdate
    - slot{"birthdate": "1997-11-23"}
    - utter_training_type
* training_confirmation{"training_type": "definition"}
    - slot{"training_type": "definition"}
    - utter_reinforce_objective
    - utter_do_you_want_routine
* deny
    - utter_do_you_want_diets
* deny
    - utter_track_progress
* deny
    - action_add_user
    - slot{"user_id": 0}
    - utter_welcome
* user_wants_to_join
    - utter_already_in

## Generated Story 8527159365261095012
* greet
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Test"}
    - slot{"measure_user": true}
    - slot{"user_gender": "male"}
    - slot{"user_id": "1"}
    - utter_greet
* user_wants_to_join
    - utter_already_in

## not initially join but after yes
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": 0}
    - utter_unknown
* deny
    - utter_not_interested
* help
    - utter_give_help
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
* confirm_birthdate{"DATE": "1995-06-26", "time": "1995-06-26T00:00:00.000+02:00"}
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
* affirm
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
    - utter_measurements_taken
    - utter_welcome

## Generated Story 724132224463034230
* greet
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Test"}
    - slot{"measure_user": true}
    - slot{"user_gender": "male"}
    - slot{"user_id": "1"}
    - utter_greet
* confirm_table{"table_type": "diet"}
    - slot{"table_type": "diet"}
    - utter_dont_understand
* confirm_table{"table_type": "exercise"}
    - slot{"table_type": "exercise"}
    - utter_dont_understand

## Generated Story 7492174187270707981
* confirm_table{"table_type": "diet"}
    - slot{"table_type": "diet"}
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Test"}
    - slot{"measure_user": true}
    - slot{"user_gender": "male"}
    - slot{"user_id": "1"}
    - utter_dont_understand

## Generated Story -7198040200321581448
* confirm_table{"table_type": "exercise"}
    - slot{"table_type": "exercise"}
    - action_check_profile
    - slot{"user_exists": true}
    - slot{"user_name": "Test"}
    - slot{"measure_user": true}
    - slot{"user_gender": "male"}
    - slot{"user_id": "1"}
    - utter_dont_understand

## Generated Story -2419908462534895410
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - slot{"user_name": null}
    - slot{"measure_user": false}
    - slot{"user_gender": null}
    - slot{"user_id": "0"}
    - utter_unknown
* affirm
    - utter_ask_name
* name_confirmation{"PERSON": "pablo"}
    - slot{"PERSON": "pablo"}
    - action_set_name
    - slot{"user_name": "Pablo"}
    - utter_nice_name
    - utter_gender_confirmation
* gender_confirmation{"user_gender": "male"}
    - slot{"user_gender": "male"}
    - utter_birthdate
* confirm_birthdate{"DATE": "the 26 of June 1995", "time": "1995-06-26T00:00:00.000+02:00"}
    - slot{"time": "1995-06-26T00:00:00.000+02:00"}
    - action_set_birthdate
    - slot{"birthdate": "1995-06-26"}
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
    - slot{"user_id": 20}
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
* form: add_bodyfatratio{"number": 13, "PERCENT": "13%"}
    - slot{"number": 13}
    - form: measurement_form
    - slot{"bodyfatratio": ["13", 13]}
    - form{"name": null}  
    - slot{"requested_slot": null}
    - utter_measurements_taken
    - utter_welcome
