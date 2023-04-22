Use pendrive with ISO with live environment

`lsblk` to see block devices
you can also use:
`lsblk -f` (see block devices fs)
`fdisk -l`
you can ignore `rom`, `loop` and `airloot`

let's assume root volume is on `/dev/sda2` partition
and `/dev/sda1` is UEFI/EFI


`mount /dev/sda2 /mnt` - to mount root volume to `/mnt`

### if btrfs:
`btrfs subvolume list -p /mnt | head -n 20` to see subvolumes
(you'll have to mount some of them - `head` prevent you from seeing hundreds of snapshots)
`umount /mnt`
`mount /dev/sda2 /mnt -o subvol=@` - by default root subvolume is named `@` but it can be named other way
`mount /dev/sda2 /mnt/var/cache -o subvol=@cache`
`mount /dev/sda2 /mnt/home -o subvol=@home`
and so on with subvolumes

`mount /dev/sda1 /mnt/boot/efi` - it use it's own fs (`fat32`)

`arch-chroot /mnt`


For encrypted systems - later
[good reference](https://discovery.endeavouros.com/system-rescue/arch-chroot-for-efi-uefi-systems/2021/03/)