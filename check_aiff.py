import struct
with open('sound/samples/sfx_mario/00.aiff', 'rb') as f:
    data = f.read()
idx = data.find(b'COMM')
channels, frames, bits = struct.unpack('>hLh', data[idx+8:idx+16])
rate_bytes = data[idx+16:idx+26]
exp = struct.unpack('>H', rate_bytes[0:2])[0]
mantissa = struct.unpack('>Q', rate_bytes[2:10])[0]
sample_rate = mantissa * (2.0 ** (exp - 16383 - 63))
print('channels:', channels, 'bits:', bits, 'sample_rate:', sample_rate)