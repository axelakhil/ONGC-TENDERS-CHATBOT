## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## category 
* show_this_category
  - action_show_by_category

## category 0
* greet
  - utter_greet
* show_this_category
  - action_show_by_category


## show_by_category
* greet
  - utter_greet
* want_to_know
  - utter_ask_id
* deny
  - utter_ask_category
* show_this_category
  - action_show_by_category 
* more_info
  - utter_more_info  

## show_by_category 1
* greet
  - utter_greet
* want_to_know
  - utter_ask_id
* deny
  - utter_ask_category
* show_this_category
  - action_show_by_category 
* show_this_category
  - action_show_by_category 
* show_this_category
  - action_show_by_category     
* more_info
  - utter_more_info    

## showid
* greet
  - utter_greet
* show_this_id
  - action_show_by_id

## showid 1
* show_this_id
  - action_show_by_id  

## show_by_id
* greet
  - utter_greet
* want_to_know
  - utter_ask_id
* affirm
  - utter_tell_id
* show_this_id
  - action_show_by_id      
* more_info
  - utter_more_info      

## show_by_id 1
* greet
  - utter_greet
* want_to_know
  - utter_ask_id
* affirm
  - utter_tell_id
* show_this_id
  - action_show_by_id 
* show_this_id
  - action_show_by_id  
* show_this_id
  - action_show_by_id         
* more_info
  - utter_more_info      


## more_information
* more_info
  - utter_more_info 

## direct_id
* greet
    - utter_greet
* show_this_id{"tend":"T16PC20001"}
    - action_show_by_id  

## New Story  1
* greet
    - utter_greet
* want_to_know
    - utter_ask_id
* deny
    - utter_ask_category
    - slot{"tender":"e-gas"}
* show_this_category{"tender":"e-gas"}
    - slot{"tender":"e-gas"}
    - action_show_by_category
    - slot{"tender":"Procurement"}
* show_this_category{"tender":"Procurement"}
    - action_show_by_category
    - slot{"tender":"Corrigendum"}
* show_this_category{"tender":"Corrigendum"}
    - action_show_by_category
    - slot{"tend":"T16PC20001"}        
* show_this_id{"tend":"T16PC20001"}
    - action_show_by_id
* more_info
    - utter_more_info
* goodbye
    - utter_goodbye

## New Story 100
    - utter_greet
* greet
    - slot{"tend":"T16PC20001"}
* show_this_id{"tend":"T16PC20001"}
    - action_show_by_id
* goodbye
    - utter_goodbye

## New Story 101
    - slot{"tend":"T16PC20001"}
* show_this_id{"tend":"T16PC20001"}
    - action_show_by_id    

