import Data.Bits

startstate = 1;
lfsr = startstate;
bit = 0;
period = 0;

-- taps: 16 14 13 11; feedback polynomial: x^16 + x^14 + x^13 + x^11 + 1 
shift =
    if lfsr /= start_state then
        let bit = (lfsr shift 0) xor (lfsr shift 2) xor (lfsr shift 3) xor (lfsr shift 5) & 1;
        lfsr = (shiftL lfst 1) or (shiftR bit 15); 
        period++

    else return 0