#!/usr/bin/env bash
export HOME=~
set -eux pipefail
mkdir -p ~/.DeepOnion
cat > ~/.DeepOnion/DeepOnion.conf <<EOF
regtest=1
txindex=1
printtoconsole=1
rpcuser=doggman
rpcpassword=donkey
rpcallowip=127.0.0.1
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28333
fallbackfee=0.0002
[regtest]
rpcbind=0.0.0.0
rpcport=18554
EOF
rm -rf ~/.DeepOnion/regtest
screen -S DeepOniond -X quit || true
screen -S DeepOniond -m -d DeepOniond -regtest
sleep 6
DeepOnion-cli createwallet test_wallet
addr=$(DeepOnion-cli getnewaddress)
DeepOnion-cli generatetoaddress 150 $addr > /dev/null
