import os
import sys
import gzip

print "hello"
list_of_files = {}
path = '/onlinelogs/DeeAppSportsService/NA/Prod/2019/08/02/00'
outf = open("/tmp/midhun/aivus.out", "w")
found = 0
m = {}
tm = 0.0
tml = ''
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if filename.startswith('service'):
            list_of_files[filename] = os.sep.join([dirpath, filename])
            inpf = gzip.open(list_of_files[filename], 'r').readlines()
            for line in inpf:
                # sys.stdout.write("%s \r" % line)
                # sys.stdout.flush()
                line = str(line).strip()
                if 'AAAClientName' in line:
                    m[line] = m.get(line, 0) + 1
                elif 'RemoteIpAddressSequence' in line:
                    m[line] = m.get(line, 0) + 1
                elif 'Time=' in line:
                    try:
                        x, v = line.split("=")
                        v = float(v.split()[0])
                        if tm < v:
                            tm = v
                            tml = line
                    except:
                        pass
            print list_of_files[filename] + ' processed'

sm = sorted(m.items(), key=lambda x:x[1])
for k, v in sm:
    outf.write("{0} : {1} \n".format(k, v))
outf.write("\n\n" + str(sum(m.values())) + "\n\n\n\n\n")
outf.write("\n\n" + str(tm) + "\n\n")
