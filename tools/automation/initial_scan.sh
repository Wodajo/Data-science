#!/usr/bin/env bash

# 					AUTOMATE INITIAL SCANS FOR A TARGET
# - create log files
# - updates "chronologically.md" file (containing markdown links to commands logs in chronological manner)
# - create main target page - IP, MAC, OS
# - banner grabbing -> log files
# - create general investigation pages for ports
# - populate investigation page & main taget page with links to log


# divide it into modules - more interactive in what you want to do
# maybe somehow objects? It would be easier to manage target-module relations
# maybe nmap -A for all ports? (I'd like it as a module)   - MAKE FUNCTION FOR IT


IP=$1
com_name="unknown"



	chron_add () {  # adds current command to chronologically page (as link)
		local generic_log  # local for later portability of this function
		local link
		generic_log="log-$T-$com_name"
		link="[$generic_log](./$generic_log.md)"
		echo "$link" >> $CHRON_LOG
		return
	}

	ping_func () {
		echo "[+] Ping..."
		local com_name="ping"
		local log="$LOGS_DIR/log-$T-$com_name.md"  # you'll have to reuse this in further functions bcos
		# when $com_name changes $log value won't automatically change (even if not local ofc)
		cat <<- _EOF_ >> $log
			$(echo "ICMP echo reply ttl IP header field: 64 linux (some kernels 255), 128 windows, 255 solaris&network")
			\`\`\`
			$(ping -c 2 $IP)
			\`\`\`
			_EOF_
		chron_add
		return
	}

	SYN_func () {
		echo "[+] SYN scan & OS detection..."
		local com_name="nmap-sS-O"
		local log="$LOGS_DIR/log-$T-$com_name.md"
		cat <<- _EOF_ >> $log
			\`\`\`
			sudo nmap -Pn -p- -sS -O $IP
			$(sudo nmap -Pn -p- -sS -O $IP)
			\`\`\`
			_EOF_
		chron_add
		return
	}

	SCTP_func () {
		echo "[+] SCTP scan..."
		local com_name="nmap-sY"
		local log="$LOGS_DIR/log-$T-$com_name.md"
		cat <<- _EOF_ >> $log
			\`\`\`
			sudo nmap -Pn -p- -sY $IP
			$(sudo nmap -Pn -p- -sY $IP)
			\`\`\`
			_EOF_
		chron_add
		return
	}

	IP_func () {
		echo "[+] IP scan..."
		local com_name="nmap-sO"
		local log="$LOGS_DIR/log-$T-$com_name.md"
		cat <<- _EOF_ >> $log
			\`\`\`
			sudo nmap -Pn -p- -sO $IP
			$(sudo nmap -Pn -p- -sO $IP)
			\`\`\`
			_EOF_
		chron_add
		return
	}

	UDP_func () {
		echo "[+] UDP scan..."
		local com_name="nmap-sU"
		local log="$LOGS_DIR/log-$T-$com_name.md"
		cat <<- _EOF_ >> $log
			\`\`\`
			sudo nmap -Pn -sU $IP
			$(sudo nmap -Pn -sU $IP)
			\`\`\`
			_EOF_
		chron_add
		return
	}


	tcp_banners () {  # version, script scan & taceroute + investigation page creation
		echo "[+] TCP ports version detection & default script scan"
		local com_name="nmap-tcp-A"  # for chron_add & output log 
		local ports="$(cat "$LOGS_DIR/log-$T-nmap-sS-O.md" | grep "open" | awk -F"/" '{print $1","}' | sort -u | tr -d "\n" | sed 's|.$||')"
		cat <<- _EOF_ >> "$LOGS_DIR/log-$T-$com_name.md"
			\`\`\`
			sudo nmap -Pn -sS -pT:$ports -A $IP
			$(sudo nmap -Pn -sS -pT:$ports -A $IP)
			\`\`\`
			_EOF_
		chron_add

		echo "[+] TCP ports investigation page updates"
		ports=$(cat "$LOGS_DIR/log-$T-nmap-sS-O.md" | grep "open" | awk -F"/" '{print $1" "}' | sort -u | tr -d "\n" | sed 's|.$||')  # local var redefinition
		for port in $ports; do
			cat <<- _EOF_ >> $T/$T-$port-tcp.md
				$(cat "$LOGS_DIR/log-$T-$com_name.md" | grep -m 1 "$port/tcp")
				
				[log-$T-$com_name.md](./logs-$T/log-$T-$com_name.md)
			_EOF_
		done
	return
	}

	sctp_banners () {
			echo "[+] SCTP ports version detection & default script scan"
		local com_name="nmap-sctp-A"
		local ports="$(cat "$LOGS_DIR/log-$T-nmap-sY.md" | grep "open" | awk -F"/" '{print $1","}' | sort -u | tr -d "\n" | sed 's|.$||')"
		cat <<- _EOF_ >> "$LOGS_DIR/log-$T-$com_name.md"
			\`\`\`
			sudo nmap -Pn -sY -pS:$ports -A $IP
			$(sudo nmap -Pn -sY -pS:$ports -A $IP)
			\`\`\`
			_EOF_
		chron_add
# ports investigation pages creation
		echo "[+] SCTP ports investigation page updates"
		ports=$(cat "$LOGS_DIR/log-$T-nmap-sY.md" | grep "open" | awk -F"/" '{print $1" "}' | sort -u | tr -d "\n" | sed 's|.$||')  # local var redefinition
		for port in $ports; do
			cat <<- _EOF_ >> $T/$T-$port-sctp.md
				$(cat "$LOGS_DIR/log-$T-$com_name.md" | grep -m 1 "$port/sctp")
				
				[log-$T-$com_name.md](./logs-$T/log-$T-$com_name.md)

			_EOF_
		done
	return
	}

	udp_banners () {
			echo "[+] UDP ports vesrion detection & default script scan"
		local com_name="nmap-udp-A"
		local ports="$(cat "$LOGS_DIR/log-$T-nmap-sU.md" | grep "open" | awk -F"/" '{print $1","}' | sort -u | tr -d "\n" | sed 's|.$||')"
		cat <<- _EOF_ >> "$LOGS_DIR/log-$T-$com_name.md"
			\`\`\`
			sudo nmap -Pn -sU -pU:$ports -A $IP
			$(sudo nmap -Pn -sU -pU:$ports -A $IP)
			\`\`\`
			_EOF_
		chron_add
# ports investigation pages creation 
		echo "[+] USP ports investigation page updates"
		ports=$(cat "$LOGS_DIR/log-$T-nmap-sU.md" | grep "open" | awk -F"/" '{print $1" "}' | sort -u | tr -d "\n" | sed 's|.$||')  # local var redefinition
		for port in $ports; do
			cat <<- _EOF_ >> $T/$T-$port-udp.md
				$(cat "$LOGS_DIR/log-$T-$com_name.md" | grep -m 1 "$port/udp")
				
				[log-$T-$com_name.md](./logs-$T/log-$T-$com_name.md)
			_EOF_
		done
	return
	}


	MAC_OS () {  # rebuild it so that it can search for MAC in many places / less hardcoding
		local com_name="nmap-sS-O"
		local log="$LOGS_DIR/log-$T-$com_name.md"
		MAC="$(cat $log | grep -m 1 "MAC Address" | cut -d " " -f 3)"  # -m only first line matching
		OS_CPE="$(cat $log | grep -m 1 "OS CPE:")"
		OS_details="$(cat $log | grep -m 1 "OS details:")"
		Net_dist="$(cat $log | grep -m 1 "Network Distance:")"
		return
	}


	target_page () {
		echo "[+] Creating $T main page"
		MAIN_PAGE="$T/$T-$IP.md"
		cat <<- _EOF_ >> $MAIN_PAGE
			IP: $IP
			MAC: $MAC
			$OS_CPE
			$OS_details


			****

			_EOF_
# investigation pages links
		local com_name="nmap-tcp-A" 
		local ports=$(cat "$LOGS_DIR/log-$T-nmap-sS-O.md" | grep "open" | awk -F"/" '{print $1" "}' | sort -u | tr -d "\n" | sed 's|.$||')
		for port in $ports; do
			cat <<- _EOF_ >> $MAIN_PAGE
				[$port/tcp](./$T-$port-tcp) $(cat "$LOGS_DIR/log-$T-$com_name.md" | grep -m 1 "$port/tcp" | cut -f 2- -d " ")
			_EOF_
		done


 		local com_name="nmap-sctp-A" 
		local ports=$(cat "$LOGS_DIR/log-$T-nmap-sY.md" | grep "open" | awk -F"/" '{print $1" "}' | sort -u | tr -d "\n" | sed 's|.$||')
		for port in $ports; do
			cat <<- _EOF_ >> $MAIN_PAGE
				[$port/sctp](./$T-$port-sctp) $(cat "$LOGS_DIR/log-$T-$com_name.md" | grep -m 1 "$port/sctp" | cut -f 2- -d " ")
			_EOF_
		done

 		local com_name="nmap-udp-A" 
		local ports=$(cat "$LOGS_DIR/log-$T-nmap-sU.md" | grep "open" | awk -F"/" '{print $1" "}' | sort -u | tr -d "\n" | sed 's|.$||')
		for port in $ports; do
			cat <<- _EOF_ >> $MAIN_PAGE
				[$port/udp](./$T-$port-udp) $(cat "$LOGS_DIR/log-$T-$com_name.md" | grep -m 1 "$port/udp" | cut -f 2- -d " ")
			_EOF_
		done


		return
	}



if [ "$IP" == "" ]; then
	echo "Scanner works only for 1 target"
	echo "Enter target IP"
	echo "Syntax: ./initial_scan.sh 192.168.4.1"

else
	echo -n "Enter target name: "  # -n for no trailing newline in output
	read T
	LOGS_DIR=$T/logs-$T
	CHRON_LOG=$LOGS_DIR/chronologically.md
	
	echo "[+] selected IP: $IP"
	if [ ! -d "$T" ]; then
		mkdir $T
	fi

	if [ ! -d "$LOGS_DIR" ]; then
		mkdir $LOGS_DIR
	fi
	
	ping_func
	SYN_func
	SCTP_func
	IP_func
	UDP_func
	tcp_banners
	sctp_banners
	udp_banners
	MAC_OS
	target_page

fi
