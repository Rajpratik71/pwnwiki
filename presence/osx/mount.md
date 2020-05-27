# Mounts and Mounting #

OSX provides the *diskutil* utility to interact with local devices and device images. The *Finder* utility is used to access remote NFS and Samba shares.

## List Mounted Devices ##

 * ``` mount ```
 * ``` ls /Volumes ```

## Mount Samba ##

 * ``` sudo mount -t nfs remote_user:/remote_mount_point /local_mount_point ``

## Mount NFS ##

 * ``` mount_smbfs //remote_user:password@server/remote_mount_point /local_mount_point ```

## Mount an ISO, Disk, VMDK ##

Mount the ISO file, VDMK file, or device

 * ``` hdiutil attach -imagekey diskimage-class=CRawDiskImage -nomount <iso, disk, vdmk> ```

NOTE: hditutil will mounts the image and attempt to location internal partitions. If the disk has multiple partitions you may get several mount points.

Mount disk partitions generated by "hdiutil attach" command 

 * ``` hdiutil mount /dev/disk2s1 ```

NOTE: Note where the partition is mounted to access it.

Unmount the partitions and file/device

 * ``` hdiutil unmount /dev/disk2s1 ```
 * ``` hdiutil detach /dev/disk2 ```