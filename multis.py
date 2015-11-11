# -*- coding: utf-8 -*-
# From https://bitcoinmagazine.com/articles/pybitcointools-multisig-tutorial-1394686325
#

from bitcoin import *

# http://ms-brainwallet.org/

#k1=sha256('text1')
#k2=sha256('text2')
#k3=sha256('text3')

k1=random_key()
k2=random_key()
k3=random_key()

# List of pk for testing
publicKey = [
'022df8750480ad5b26950b25c7ba79d3e37d75f640f8e5d9bcd5b150a0f85014da',
'03e3818b65bcc73a7d64064106a859cc1a5a728c4345ff0b641209fba0d90de6e9',
'021f2f6e1e50cb6a953935c3601284925decd3fd21bc445712576873fb8c6ebc18'
]

publicKey[0] = privtopub(k1)
publicKey[1] = privtopub(k2)
publicKey[2] = privtopub(k3)


# Sorting public keys to calcutate script_ = mk_multisig_script (p1,p2,p3,2,3)
publicKey.sort(key=str.lower)

p1 = publicKey[0]
p2 = publicKey[1]
p3 = publicKey[2]

#print encode_privkey (k1,'wif_compressed')

print privkey_to_address (k1),k1
print privkey_to_address (k2),k2
print privkey_to_address (k3),k3
print 
print p1
print p2
print p3

script_ = mk_multisig_script (p1,p2,p3,2,3)

address= scriptaddr (script_)

print script_
print address 

inputs = unspent (address)

if len(inputs) > 0:
    
    i = len(inputs) -1 
    inputs = inputs[i]['output']
    
    print inputs
    
    outputs = '1AkJ4gy3iky1jvhmFn6aBPn8RMABxGELsP:30000'

    tx = mktx(inputs, outputs)

    print tx
    
    sig1 = multisign (tx, 0, script_, k1)
    sig2 = multisign (tx, 0, script_, k3)
    
    tx2 = apply_multisignatures (tx,0,script_,sig1,sig2)
    
    print tx2

    # pushtx (tx2)
    
    
