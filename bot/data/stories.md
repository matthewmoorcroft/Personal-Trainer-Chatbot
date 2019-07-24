## Known user
* greet
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

## Not interested
  * not_interested
      - utter_not_interested

## New user Happy Path
  * new_user
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
  * user_wants_routine{"wants_routine": "true"}
      - slot{"wants_routine": "true"}
      - utter_reminder_routine
      - utter_do_you_want_diets
  * confirm_diets{"wants_diets": "true"}
      - slot{"wants_diets": "true"}
      - utter_confirm_diets
      - utter_track_progress
  * confirm_measurements{"measure_user": "true"}
      - slot{"measure_user": "true"}
      - action_add_user
      - utter_ask_measure_now
  * confirm_measuring_now{"measure_now":"true"}
      - slot{"measure_now":"true"}
      - utter_ask_eaten
  * confirm_eaten{"user_eaten": "false"}
      - slot{"user_eaten": "false"}
      - measurement_form
      - form{"name": "measurement_form"}
      - form{"name": null}
      - utter_welcome

## New user Happy Path II
  * new_user
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
  * user_wants_routine{"wants_routine": "false"}
      - slot{"wants_routine": "false"}
      - utter_do_you_want_diets
  * confirm_diets{"wants_diets": "false"}
      - slot{"wants_diets": "false"}
      - utter_track_progress
  * confirm_measurements{"measure_user": "true"}
      - slot{"measure_user": "true"}
      - action_add_user
      - utter_ask_measure_now
  * confirm_measuring_now{"measure_now":"true"}
      - slot{"measure_now":"true"}
      - utter_ask_eaten
  * confirm_eaten{"user_eaten": "true"}
      - slot{"user_eaten": "true"}
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
* new_user
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
* user_wants_routine{"wants_routine": "true"}
    - slot{"wants_routine": "true"}
    - utter_reminder_routine
    - utter_do_you_want_diets
* confirm_diets{"wants_diets": "true"}
    - slot{"wants_diets": "true"}
    - utter_confirm_diets
    - utter_track_progress
* confirm_measurements{"measure_user": "false"}
    - slot{"measure_user": "false"}
    - action_add_user
    - utter_welcome
