# Conan Testing

You can retrieve your password from: https://JFROG_URL.jfrog.io/ui/quick-setup

```bash
conan remote add conan-fm https://JFROG_URL.jfrog.io/artifactory/api/conan/conan
CONAN_REVISIONS_ENABLED=1 conan user -p <password> -r conan-fm admin
```

```bash
conan create .

CONAN_REVISIONS_ENABLED=1 conan upload Unity -r conan-fm --all
# Are you sure you want to upload 'Unity/2.5.2' to 'conan-fm'? (yes/no): yes
# Uploading to remote 'conan-fm':
# Uploading Unity/2.5.2 to remote 'conan-fm'                                               
# Uploaded conan_export.tgz -> Unity/2.5.2 [0.26k]                                         
# Uploaded conanfile.py -> Unity/2.5.2 [1.11k]                                             
# Uploaded conanmanifest.txt -> Unity/2.5.2 [0.10k]                                        
# Uploaded conan recipe 'Unity/2.5.2' to 'conan-fm': https://JFROG_URL.jfrog.io/artifactory/api/conan/conan
# Uploading package 1/1: d3058fa461095e3b567f10d3a72b4fac1de53cda to 'conan-fm'            
# Compressing conan_package.tgz completed [157 files]                                      
# Uploaded conan_package.tgz -> Unity/2.5.2:d305 [278.10k]                                 
# Uploaded conaninfo.txt -> Unity/2.5.2:d305 [0.38k]                                       
# Uploaded conanmanifest.txt -> Unity/2.5.2:d305 [10.49k]
```
