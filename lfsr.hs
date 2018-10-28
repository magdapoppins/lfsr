import Data.Map (Map)
import qualified Data.Map as Map 
import Data.Bits

startstate = [0,1,0,1];
feedbackRegister = [0,0,1,0]; -- Next state from startstate
counter = 0;
cipherbits = []

-- taps: 0 and 2

-- lfsr by recursion:
-- if register != startstate then 
    -- cipherbits ++ last register (Add last element from register to cipher)
    -- tap1 xor tap2 : register (Add new element to list) 
    -- drop last register (Drop the last element)
    -- counter ++
    -- else return cipherbits


shift =
    if feedbackRegister /= startstate
        then 
            cipherbits ++ last feedbackRegister
            feedbackRegister[0] xor feedbackRegister[2] : feedbackRegister
            counter + 1
        else 
            counter

        
    
    
