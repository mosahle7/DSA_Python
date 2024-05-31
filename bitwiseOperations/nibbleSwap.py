def nibbleSwap(n):
    byte = n& 0xFF
    lowN = (byte & 0x0F)<<4
    highN = (byte & 0xF0)>>4
    return lowN | highN
