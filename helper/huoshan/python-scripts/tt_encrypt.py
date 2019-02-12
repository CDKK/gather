#!/usr/local/bin/python3
import json
import gzip
import zlib
import sys

# data encrypt
def tt_encrypt(
        data,
        key=b'!*ss!_defaul%t54k&ey',
        sbox0=b'\x63\x7c\x77\x7b\xf2\x6b\x6f\xc5\x30\x01\x67\x2b\xfe\xd7\xab\x76\xca\x82\xc9\x7d\xfa\x59\x47\xf0\xad\xd4\xa2\xaf\x9c\xa4\x72\xc0\xb7\xfd\x93\x26\x36\x3f\xf7\xcc\x34\xa5\xe5\xf1\x71\xd8\x31\x15\x04\xc7\x23\xc3\x18\x96\x05\x9a\x07\x12\x80\xe2\xeb\x27\xb2\x75\x09\x83\x2c\x1a\x1b\x6e\x5a\xa0\x52\x3b\xd6\xb3\x29\xe3\x2f\x84\x53\xd1\x00\xed\x20\xfc\xb1\x5b\x6a\xcb\xbe\x39\x4a\x4c\x58\xcf\xd0\xef\xaa\xfb\x43\x4d\x33\x85\x45\xf9\x02\x7f\x50\x3c\x9f\xa8\x51\xa3\x40\x8f\x92\x9d\x38\xf5\xbc\xb6\xda\x21\x10\xff\xf3\xd2\xcd\x0c\x13\xec\x5f\x97\x44\x17\xc4\xa7\x7e\x3d\x64\x5d\x19\x73\x60\x81\x4f\xdc\x22\x2a\x90\x88\x46\xee\xb8\x14\xde\x5e\x0b\xdb\xe0\x32\x3a\x0a\x49\x06\x24\x5c\xc2\xd3\xac\x62\x91\x95\xe4\x79\xe7\xc8\x37\x6d\x8d\xd5\x4e\xa9\x6c\x56\xf4\xea\x65\x7a\xae\x08\xba\x78\x25\x2e\x1c\xa6\xb4\xc6\xe8\xdd\x74\x1f\x4b\xbd\x8b\x8a\x70\x3e\xb5\x66\x48\x03\xf6\x0e\x61\x35\x57\xb9\x86\xc1\x1d\x9e\xe1\xf8\x98\x11\x69\xd9\x8e\x94\x9b\x1e\x87\xe9\xce\x55\x28\xdf\x8c\xa1\x89\x0d\xbf\xe6\x42\x68\x41\x99\x2d\x0f\xb0\x54\xbb\x16',
        sbox1=b'\x52\x09\x6a\xd5\x30\x36\xa5\x38\xbf\x40\xa3\x9e\x81\xf3\xd7\xfb\x7c\xe3\x39\x82\x9b\x2f\xff\x87\x34\x8e\x43\x44\xc4\xde\xe9\xcb\x54\x7b\x94\x32\xa6\xc2\x23\x3d\xee\x4c\x95\x0b\x42\xfa\xc3\x4e\x08\x2e\xa1\x66\x28\xd9\x24\xb2\x76\x5b\xa2\x49\x6d\x8b\xd1\x25\x72\xf8\xf6\x64\x86\x68\x98\x16\xd4\xa4\x5c\xcc\x5d\x65\xb6\x92\x6c\x70\x48\x50\xfd\xed\xb9\xda\x5e\x15\x46\x57\xa7\x8d\x9d\x84\x90\xd8\xab\x00\x8c\xbc\xd3\x0a\xf7\xe4\x58\x05\xb8\xb3\x45\x06\xd0\x2c\x1e\x8f\xca\x3f\x0f\x02\xc1\xaf\xbd\x03\x01\x13\x8a\x6b\x3a\x91\x11\x41\x4f\x67\xdc\xea\x97\xf2\xcf\xce\xf0\xb4\xe6\x73\x96\xac\x74\x22\xe7\xad\x35\x85\xe2\xf9\x37\xe8\x1c\x75\xdf\x6e\x47\xf1\x1a\x71\x1d\x29\xc5\x89\x6f\xb7\x62\x0e\xaa\x18\xbe\x1b\xfc\x56\x3e\x4b\xc6\xd2\x79\x20\x9a\xdb\xc0\xfe\x78\xcd\x5a\xf4\x1f\xdd\xa8\x33\x88\x07\xc7\x31\xb1\x12\x10\x59\x27\x80\xec\x5f\x60\x51\x7f\xa9\x19\xb5\x4a\x0d\x2d\xe5\x7a\x9f\x93\xc9\x9c\xef\xa0\xe0\x3b\x4d\xae\x2a\xf5\xb0\xc8\xeb\xbb\x3c\x83\x53\x99\x61\x17\x2b\x04\x7e\xba\x77\xd6\x26\xe1\x69\x14\x63\x55\x21\x0c\x7d'
):
    # data = '{"_gen_time":1532598343824,"header":{"access":"wifi","aid":1112,"appkey":"56ea65c067e58eea7e000c63","display_name":"火山小视频","not_request_sender":0,"package":"com.ss.android.ugc.live","release_build":"dfa0993_20180620","sdk_version":"2.5.4.0","sig_hash":"aea615ab910015038f73c47e45d21466","build_serial":"49176505","clientudid":"3fdfa56d-e8ec-2a5d-431e-a2257c67a86a","cpu_abi":"armeabi-v7a","density_dpi":480,"device_brand":"Xiaomi","device_manufacturer":"Xiaomi","device_model":"MI 4LTE","display_density":"mdpi","language":"zh","mc":"A2:6A:A0:A6:72:EE","openudid":"53d4e91578487185","os":"Android","os_api":23,"os_version":"6.0.1","region":"CN","resolution":"1080x1920","rom":"MIUI-7.11.30","rom_version":"miui_V9_7.11.30","serial_number":"49176505","sim_serial_number":[],"timezone":8,"tz_name":"Asia/Shanghai","tz_offset":28800,"udid":"502025975825073","app_version":"4.2.0.3","channel":"xiaomi","manifest_version_code":4203,"update_version_code":4203,"version_code":4203},"magic_tag":"ss_app_log"}'
    def ROR(bytes, start, end, byte):
        r = bytes[start:end]
        b = len(r) - byte
        r = r[b:] + r[:b]
        return bytes[0:start] + r + bytes[end:len(bytes)]
    if not isinstance(key, bytearray):
        key = bytearray(key)
    while True:
        if len(key) < 16:
            key.append(sbox1[key[len(key) - 1]])
        else:
            key = key[0:16].translate(sbox0)
            break
    input = gzip.compress(data.encode('utf-8', 'surrogateescape'))
    output = bytearray(input)
    headers = [31, 139, 8, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(headers)):
        output[i] = headers[i]
    fill = (-len(input)) & 15
    output.extend(bytearray(fill))
    output = output.translate(sbox0)
    for i in range(int(len(output) / 16)):
        i *= 16
        output = ROR(output, i + 4, i + 8, 3)
        output = ROR(output, i + 8, i + 12, 2)
        output = ROR(output, i + 12, i + 16, 1)
        for j in range(16):
            output[i + j] ^= key[j]
    return bytes([116, 99, 2, fill]) + bytes(output)

def main():
    result = tt_encrypt(sys.argv[1])
    result = "".join(map(chr, result)) # 转成str进行传输 此方案不用考虑编码
    print(result)
    sys.stdout.flush()
    # return result

if __name__ == '__main__':
    main()

