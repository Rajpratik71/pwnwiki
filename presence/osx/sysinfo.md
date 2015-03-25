<!-- Code for collapse and expand -->
<script type="text/javascript"> 
$(document).ready(function() { 
$('div.view').hide(); 
$('div.slide').click(function() {
$(this).next('div.view').slideToggle('fast'); 
return false; 
}); 
}); 
</script>

# OS X System Information Gathering

Access to a system can be acquired in any number of ways. Shell access provides command line access while RDP/VNC access will provide the user a GUI interface. Acquiring system data is different is slightly different depending on the type of access..

Command line programs demonstrated below are provided in the form to provide information quickly. Use the commands help (-h or --help) or man page to understand the commands full functionality. You may be surprised with what you find.

## Command Line Access

### Screen Shot ###

Quick screen shot using the *screencapture* command with one second (default is 5) delay and no sound. 

 * ``` screencapture -x -T 1 ~/.ing/screenshot.png ```
 
 NOTE: Getting a single unfocused window using the Window ID isn't simple: http://apple.stackexchange.com/questions/56561/how-do-i-find-the-windowid-to-pass-to-screencapture-l 

### User Accounts ###

There are several ways to get at user accounts besides listing them. Check login prompts and mounted devices. In the case of the later, the username AND password might be exposed in the mounting command.

List All Accounts

 * ``` dscacheutil -q user ```
 * ``` cat /private/etc/master.password ```

List User Accounts

 * ``` 'dscacheutil -q user | grep -A 3 -B 2 -e uid:\ 5'[0-9][0-9]' ' ```

Dump passwords

 * ``` sudo dscl . read /Users/<user>/ AuthenticationAuthority ```
 * ``` sudo dscl . read /Users/<user>/ dsAttrTypeNative:ShadowHashData ``` 
 
  NOTE: requires Administrative privileges

OS X Operating System Version

 * ``` sw_vers ```
 * ``` sw_vers -productVersion ```

### System information ###

Generate a text report with the standard detail level.

 * ``` system_profiler ```

Generate a report with detailed system information including user, boot volume, version, kernel information.

 * ``` system_profiler SPSoftwareDataType ```
 
List ALL available information (very detailed) 

 * ``` system_profiler -detailLevel full ```

### Network Information ###
OS X tool that provides network information and will even scan for local wireless networks

 * ``` system_profiler ```

List network interfaces

 * ``` ifconfig ```
 * ``` scutil --nwi ``` 

Wireless interface, network scan, and connection

* ``` /System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -I ```
* ``` /System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -s ```
* ``` networksetup -setairportnetwork en1 <SSID> <PASSWORD> ```

Routes

 * ``` netstat -r  ```

DNS

 * ``` scutil --dns ```

Proxy

 * ``` scutil --proxy  ```

VPN

 * ``` scutil --vpn ```

Systems on local network

 * ``` arp -a ```
 * ``` arp -i en0 -a ```

SMB

 * ``` smbutil -v status -ae <ip> ```
 * ``` for i in `arp -a | cut -d' ' -f2 | cut -d'(' -f2 | cut -d')' -f1`; do smbutil -v status -ae $i; done ```

### Mounts ###

#### List Mounted Devices ####

 * ``` mount ```
 * ``` ls /Volumes ```

