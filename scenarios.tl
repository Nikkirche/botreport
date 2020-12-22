# There are the patterns for gemrated text
start
type = "YELLOW_CARD"
And so {player} gets a yellow card.
{player} skhlopotal "gorchichnik"
{player} gets a penalty! For now just a yellow card
type = "YELLOW_RED_CARD"
Another yellow card! {player} is sent off from the field!
{player} gets a second "gorchichnik" – one less player for {active}.
type = "RED_CARD"
{player} from {active} got a card, first and last
Aim, trigger-knock your opponent down! {player} from {active} gets a red card
type = "GOAL"
GOOOOOAL!!! {player}!!!{score_active}:{score_passive}! Now that’s what I call football!
GOOOOOAL!!! {player}!{score_active}:{score_passive}! Where’s the defense of {passive} gone?
type = "OWN_GOAL"
The player has done an incredible thing! {player} brought in your gate!
type = "GOAL_PENALTY"
{player} from {active} scored from the penalty spot.
{player} from {active} pulled a penalty
exit
# After exit nothing will be accepted!
# Write the patterns after type line
# DO NOT CHANGE TYPE LINES
# all variables must be in {} and be one of this - player, time, id_in_match,active, passive,score_active, score_passive
