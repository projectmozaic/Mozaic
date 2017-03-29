import subprocess
import os
import ConfigParser

#source the variable to the terminal
pipe = subprocess.Popen('. moc_openrc.sh; env', stdout=subprocess.PIPE, shell=True)
output = pipe.communicate()[0]
env = dict((line.split("=", 1) for line in output.splitlines()))
os.environ.update(env)

image_dict = [[]]
flavor_dict = [[]]

selected_img = ''
selected_flv = ''
slected_imgid = ''
selected_flvid = ''

#save down the image list and flavor list
with open('user_credential', 'wb') as f:
    p = subprocess.Popen('openstack image list', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print "Your image list:"
    for line_idx, line in enumerate(p.stdout.readlines()):
        f.write(line)
        print line
        image_dict.append(line.split("|"))
        for img_idx,img in enumerate(image_dict[line_idx]):
            image_dict[line_idx][img_idx] = img.strip(' ')
    
    #cleanup the data
    image_dict.pop(0)
    image_dict.pop(0)
    image_dict.pop(0)
    image_dict.pop(0)
    image_dict.pop(len(image_dict)-1)

    for line_idx, img_line in enumerate(image_dict):
        image_dict[line_idx].remove('')
        image_dict[line_idx].remove('\n')

    #print image_dict

    for img_line in image_dict:
        for img_info in img_line:
            if not img_info == '\n' and not img_info == '':
                f.write(img_info + ', ')
        f.write('\n')
    #print image_dict
    #select desired image
    selected_img = raw_input("Please enter image name: ")
    print "You selected", selected_img


    p = subprocess.Popen('openstack flavor list', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print "Your flavor list:"
    for line_idx, line in enumerate(p.stdout.readlines()):
        f.write(line)
        print line
        flavor_dict.append(line.split("|"))
        for flv_idx,flv in enumerate(flavor_dict[line_idx]):
            flavor_dict[line_idx][flv_idx] = flv.strip(' ')
    
    #cleanup data
    flavor_dict.pop(0)
    flavor_dict.pop(0)
    flavor_dict.pop(0)
    flavor_dict.pop(0)
    flavor_dict.pop(len(flavor_dict)-1)

    for line_idx, flv_line in enumerate(flavor_dict):
        flavor_dict[line_idx].remove('')
        flavor_dict[line_idx].remove('\n')

    #print flavor_dict

    for flv_line in flavor_dict:
        for flv_info in flv_line:
            if not flv_info == '\n' and not flv_info == '':
                f.write(flv_info + ', ')
        f.write('\n')
    #select desired flavor
    selected_flv = raw_input("Please enter flavor name: ")
    print "You selected ", selected_flv

for img in image_dict:
    if selected_img in img:
        slected_imgid = img[0]


for flv in flavor_dict:
    if selected_flv in flv:
        slected_flvid = flv[0]

# print slected_imgid
# print slected_flvid

#type in other nessesary information
keypair_name = raw_input("Please enter keypair name: ")
print "You entered ", keypair_name

ins_name = raw_input("Please enter instance name: ")
print "You entered ", ins_name

#create the instance
p = subprocess.Popen('openstack server create --flavor '+slected_flvid+' --image '+ slected_imgid
            +' --security-group ssh --key-name '+keypair_name+ ' '+ ins_name, shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

#associate the IP address with the instance
is_public = raw_input("Do you need public IP for the instance: ")
if is_public == 'yes':
    print "You entered yes"
    p = subprocess.Popen('openstack floating ip list', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print "Your ip list:"
    for line_idx, line in enumerate(p.stdout.readlines()):
        print line
    bind_ip = raw_input("Enter the IP address you want to bind: ")
    p = subprocess.Popen('openstack server add floating ip ' + ins_name +' ' + bind_ip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
else:
    print "You entered no"