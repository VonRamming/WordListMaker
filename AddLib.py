import hashlib as hb
import os


def get_unique_filename(name):
    counter = 1
    y = name.rsplit('.', 1)[0]
    name = y
    names = ['' for _ in range(12)]
    i = 0
    lib = ["MD5","SHA256","SHA512","SHA384","SHA1","SHA224","SHA3_256","SHA3_512","SHA3_224","SHA3_384","SHA3_512","SHA3_224"]
    while os.path.exists(f"./Out/{name}Out.txt"):
        name = f"{y}({counter})"
        counter += 1
    counter = 1
    for i in range(len(lib)):
        while os.path.exists(f"./Out/{names[i]}{lib[i]}Out.txt"):
            names[i] = f"{y}({counter})"
            counter += 1
        counter = 1
    return name, names



print ('\n',
        "----Wordlist Creator----",
    '\n')
name_ = [''] * 12
print("Supports: MD5, SHA256, SHA512, SHA384, SHA1, SHA224, SHA3_256, SHA3_512, SHA3_224, SHA3_384, SHA3_512, SHA3_224, SHA3_384")
path = input("Give that path which u put wordlist it in : ")
option = input("Enter the option (default: 1)(1-OneFileAllTypesOfHash)(2-OneFileOneTypeOfHash): ") or '1'
encoding = input("Enter the encoding (default: utf-8): ") or 'utf-8'
name ,name_ = get_unique_filename(path)

try:
    with open(path,"+r") as file:
        for satir in file:
            satir = satir.strip()  # Remove whitespace/newlines
            satir = satir.encode(encoding=encoding)  # Explicitly specify encoding
            if option == '1':
                try:
                    with open(f"./Out/{name}Out.txt","a") as file:
                        file.write(hb.md5(satir).hexdigest() + "\n")
                        file.write(hb.sha256(satir).hexdigest() + "\n")
                        file.write(hb.sha512(satir).hexdigest() + "\n")
                        file.write(hb.sha384(satir).hexdigest() + "\n")
                        file.write(hb.sha1(satir).hexdigest() + "\n")
                        file.write(hb.sha224(satir).hexdigest() + "\n")
                        file.write(hb.sha3_256(satir).hexdigest() + "\n")
                        file.write(hb.sha3_512(satir).hexdigest() + "\n")
                        file.write(hb.sha3_224(satir).hexdigest() + "\n")
                        file.write(hb.sha3_384(satir).hexdigest() + "\n")
                        file.write(hb.sha3_512(satir).hexdigest() + "\n")
                except Exception as e:
                        print(e)
            elif option == '2':
                with open(f"./Out/{name_[0]}MD5Out.txt","a") as file:
                    file.write(hb.md5(satir).hexdigest() + "\n")
                with open(f"./Out/{name_[1]}SHA256Out.txt","a") as file:
                    file.write(hb.sha256(satir).hexdigest() + "\n")
                with open(f"./Out/{name_[2]}SHA512Out.txt","a") as file:
                    file.write(hb.sha512(satir).hexdigest() + "\n")
                with open(f"./Out/{name_[3]}SHA384Out.txt","a") as file:
                    file.write(hb.sha384(satir).hexdigest() + "\n")
                with open(f"./Out/{name_[4]}SHA1Out.txt","a") as file:
                    file.write(hb.sha1(satir).hexdigest() + "\n")
                with open(f"./Out/{name_[5]}SHA224Out.txt","a") as file:
                    file.write(hb.sha224(satir).hexdigest() + "\n")
                with open(f"./Out/{name_[6]}SHA3_256Out.txt","a") as file:
                    file.write(hb.sha3_256(satir).hexdigest() + "\n")
                with open(f"./Out/{name_[7]}SHA3_512Out.txt","a") as file:
                    file.write(hb.sha3_512(satir).hexdigest() + "\n")
                with open(f"./Out/{name_[8]}SHA3_224Out.txt","a") as file:
                    file.write(hb.sha3_224(satir).hexdigest() + "\n")
                with open(f"./Out/{name_[9]}SHA3_384Out.txt","a") as file:
                    file.write(hb.sha3_384(satir).hexdigest() + "\n")
                with open(f"./Out/{name_[10]}SHA3_512Out.txt","a") as file:
                    file.write(hb.sha3_512(satir).hexdigest() + "\n")
except Exception as e:
    print(e)
