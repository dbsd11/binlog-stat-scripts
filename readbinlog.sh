mysqlbinlog --read-from-remote-server --raw --host=${slaveHost} --user=${readUser} --stop-never ${firstBinLog} --result-file=/tmp/binlog/ -p

cp -r /tmp/binlog/* .
