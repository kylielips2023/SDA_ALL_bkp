#!/bin/bash

	# if user is not running the command as root
	if [ "$UID" -ne 0 ]; then

		# output message
		echo "Please run the installer with SUDO!"

		# stop script
		exit
	fi

	# check update
	apt update > /dev/null 2>&1

	# output message
	echo -e "\nCyberGhost Installer ...\n"


	# define required packages
    requiredPackages=(curl openvpn resolvconf wireguard)

	# loop through packages
    for package in "${requiredPackages[@]}"; do

		# set package
		p="$package"

		# if package is opwireguardenvpn
		if [ "$package" == "wireguard" ]; then

			# check if wireguard ppa exist
			responseCode=$(grep ^ /etc/apt/sources.list /etc/apt/sources.list.d/* | grep -c wireguard)

			# if ppa does not exist
			if [ "$responseCode" == "0" ]; then

				# install wireguard ppa
				add-apt-repository -y ppa:wireguard/wireguard > /dev/null 2>&1
				apt update > /dev/null 2>&1
			fi

			# change package name
			p="wg"
		fi

		# check if package is installed and get exit code
        responseCode=$(which "$p" > /dev/null 2>&1; echo "$?")

		# output message
		echo -n "Check if \"$package\" package is already installed ... "

		# if package is installed
        if [ "$responseCode" == "0" ]; then

			# output message
			echo "Yes"

			# if package is openvpn
			if [ "$package" == "openvpn" ]; then

				# get openvpn version
				openvpnVersion=$(openvpn --version | head -n 1 | awk '{print $2}')

				# get major version
				majorVersion=$(echo "$openvpnVersion" | awk -F. '{print $1}')

				# get minor version
				minorVersion=$(echo "$openvpnVersion" | awk -F. '{print $2}')

				# output message
				echo -n "Checking OpenVPN version ... "

				if [ $majorVersion -ge 2 ] && [ $minorVersion -gt 3 ]; then

					# output message
					echo "Latest ..."
				else

					# output message
					echo "The OpenVPN version is too old ... "
					echo "Removing old package ... "

					# uninstall package
					apt remove "$package" -y > /dev/null 2>&1

					# output message
					echo -n "Installing new package ... "
					curl -s https://swupdate.openvpn.net/repos/repo-public.gpg | apt-key add -
					echo "deb http://build.openvpn.net/debian/openvpn/stable xenial main" > /etc/apt/sources.list.d/openvpn-aptrepo.list
					apt update > /dev/null 2>&1
					apt install "$package" -y > /dev/null 2>&1

					# output message
					echo "Done."
				fi
			fi
        else

			# output message
            echo -n "No, installing ... "

			if [ "$package" == "openvpn" ]; then

				# get openvpn version from apt
				openvpnVersion=$(apt show openvpn|grep "Version:" | awk '{ print $2 }')
				version=$(echo "$openvpnVersion"| awk -F'-' '{print $1}')
				
				# get major version
				majorVersion=$(echo "$version" | awk -F. '{print $1}')

				# get minor version
				minorVersion=$(echo "$version" | awk -F. '{print $2}')

				# if version is lower then 2.4
				if [ $majorVersion -ge 2 ] && [ $minorVersion -lt 4 ]; then
					curl -s https://swupdate.openvpn.net/repos/repo-public.gpg | apt-key add -
					echo "deb http://build.openvpn.net/debian/openvpn/stable xenial main" > /etc/apt/sources.list.d/openvpn-aptrepo.list
					apt update > /dev/null 2>&1
				fi
			fi


			# install package
            apt install "$package" -y > /dev/null 2>&1

			# output message
            echo "Done."
        fi
    done

	# output message
	echo "Continue ..."

	# if directory exist
	if [ -d /usr/local/cyberghost ]; then

		# remove directory
		rm -rf /usr/local/cyberghost
	fi

	echo "Installing application ..."

	# if logs directory does not exist
	if [ ! -d /usr/local/cyberghost ]; then

		# create logs directory if not exist
		mkdir /usr/local/cyberghost
	fi

	# copy certificates to local directory
	cp -r /usr/local/cyberghost/openvpn/cyberghostvpn-ubuntu/cyberghost/* /usr/local/cyberghost

	# change directory permissions
	chmod -R 755 /usr/local/cyberghost

	# output message
	echo "Create symlinks ..."

	# if symlink exist
	if [ -L /usr/bin/cyberghostvpn ]; then

		# remove old symlink
		rm /usr/bin/cyberghostvpn
	fi

	# create symlink
	ln -sf /usr/local/cyberghost/cyberghostvpn /usr/bin/cyberghostvpn

	# setup application
	cyberghostvpn --setup
