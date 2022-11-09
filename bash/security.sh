
touch security_information
ls -Ra * >security_information
vmstat -s |  awk '{if(NR==2) print $0}' | cut -d' ' -f7- >> security_information
lsblk >> security_information
lspci>> security_information
lsusb    >> security_information
mpstat >> security_information
df >> security_information
cat etc/sysctl.conf >> security_information
