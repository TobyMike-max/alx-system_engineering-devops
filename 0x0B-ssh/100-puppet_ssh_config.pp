# Uses puppet to edit /etc/ssh/ssh_config file

$str = "IdentityFile ~/.ssh/school
	PasswordAuthentication no
	Include /etc/ssh/sshd_config.d/*.conf
	ChallengeResponseAuthentication no
	X11Forwarding yes
	PrintMotd no
	AcceptEnv LANG LC_*
	Subsystem       sftp    /usr/lib/openssh/sftp-server
	"

file { '/etc/ssh/ssh_config':
	content => $str
}
