# multisign
https://bitcoinmagazine.com/articles/pybitcointools-multisig-tutorial-1394686325
...........................................................................................................

There has been a large amount of interest in multisignature transaction technology in the past year, especially with the recent announcement of CryptoCorp. If you want to play with multisig technology yourself on the command line, here are the gritty details of how to do it. First, run sudo pip install bitcoin to install the Python Bitcoin library. Then, to generate the three private keys, run the following:

> k1=`pybtctool random_key`> k2=`pybtctool random_key`> k3=`pybtctool random_key`> p1=`pybtctool privtopub $k1`> p2=`pybtctool privtopub $k2`> p3=`pybtctool privtopub $k3`

You now have three private keys and three public keys; run echo $k1, echo $p3, etc to see these values in the raw form. Now, we make the multisig script and address:

> script=`pybtctool mk_multisig_script $p1 $p2 $p3 2 3`> address=`pybtctool scriptaddr $script`

Let’s see what these values are:

> echo $script5241045f4af45e3a7a86393c4ab9540cca382d46f10345b3ffcbb058089788550d167b7c079870d00da9728f8589fa5bbe0a8d62eadd56d37f3be6bc8145fe9a27437b4104509394eade56d900e90146e4bdf14f567b845ab0da986476253fe438f12032a248bbf2c16d28409b2961b3a3f797832ad195a8cef96589371271e2df6195cf804104ef6c434a854996e63cf650c0ba813993e90eef564bc78ad14768de51ac6b1bb00c5fe3381a923567162e8821e86ee28fbe4a25325f59cf6ede87c15d5af2881e53ae> echo $address3DDifvXMEQBEvn7dVR1wF5RXveA5MxEXek

Due to randomness, your values will be different, but of the same general form. Notice the 3 at the start of the address. Now, send some BTC to your address, and run the following to make sure you actually received the funds.

> pybtctool unspent $address[{"output": "9e123938b7625ef7807f31ad61c3b818484fed93eb951d981abd83413005080f:0", "value": 20000}]

Now, we can make the transaction, sending the funds to the Methuselah Foundation‘s donation address:

> tx=`pybtctool mktx 9e123938b7625ef7807f31ad61c3b818484fed93eb951d981abd83413005080f:0 1GRF5cmvAqQPNVPRHe1TpMZGS1mYFHFQHu:10000`> echo $tx01000000010f0805304183bd1a981d95eb93ed4f4818b8c361ad317f80f75e62b73839129e0000000000ffffffff0110270000000000001976a914a91f9f763b29340b7d15fddd8b6ee41ac56fc88d88ac00000000

Now, let’s sign it with keys 1 and 3:

> sig1=`pybtctool multisign $tx 0 $script $k1`> sig2=`pybtctool multisign $tx 0 $script $k3`> tx2=`pybtctool apply_multisignatures $tx 0 $script $sig1 $sig2`

The final transaction looks like this:

> echo $tx201000000010f0805304183bd1a981d95eb93ed4f4818b8c361ad317f80f75e62b73839129e00000000fd5f01004930460221009e4cc93850d3d7ed6fcdd416f13b4f652d80c00d6c76f7594645540fb7ece79d022100f9cb6ec2ca973c2ef52aa541bbe28aa038189116de94df68fc29b0901b472f2f0148304502201bd655c130e6f47567f8e7d7b769d974d8b543ec53bf99d2232d07253af832c0022100f49d1f0564c9b0b192bd178b36ab04818ed1673feae380c46ce5c8dbaa622f1f014cc95241045f4af45e3a7a86393c4ab9540cca382d46f10345b3ffcbb058089788550d167b7c079870d00da9728f8589fa5bbe0a8d62eadd56d37f3be6bc8145fe9a27437b4104509394eade56d900e90146e4bdf14f567b845ab0da986476253fe438f12032a248bbf2c16d28409b2961b3a3f797832ad195a8cef96589371271e2df6195cf804104ef6c434a854996e63cf650c0ba813993e90eef564bc78ad14768de51ac6b1bb00c5fe3381a923567162e8821e86ee28fbe4a25325f59cf6ede87c15d5af2881e53aeffffffff0110270000000000001976a914a91f9f763b29340b7d15fddd8b6ee41ac56fc88d88ac00000000

And now we push:

> pybtctool eligius_pushtx $tx277afa6140a678f4791e4566e2f15a41e7d9236c79b0abc6388e73e055af0aeec

And there we go, we’re 0.0001 BTC closer to at least mitigating the effect of the single most deadly disease on the planet.
