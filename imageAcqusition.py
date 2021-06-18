import cv2
import time as tm
import paramiko
cam = cv2.VideoCapture(0)
while(True):
    return_value,image = cam.read()
    cv2.imwrite("images_taken" ,image)
    #cam.release()
    cv2.destroyAllWindows()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname = 'ip_adress', username='username', password='password', port = 22)
    ftp_client = ssh.open_sftp()
    ftp_client.put('images_taken','incoming_image')
    tm.sleep(15)
    
    



    
    
    
    
    