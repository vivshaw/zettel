---
tags: cloud, aws
---

- **Key Management Service** is a regional, public service that creates, stores, and manages keys
- can work with both symmetric and asymmetric keys
- keys never leave KMS! encryption and decryption happens within the service. this is FIPS 140-2 compliant, level 2
- keys can be AWS owned (owned and managed by an AWS service) or customer-owned. customer-owned keys can be AWS-managed (created automatically by AWS services on your behalf) or customer-managed (created explicitly by you)
- types  of keys:
	- **KMS keys** are logical, and backed by physical data. they can be generated within KMS, or imported. they can be used to encrypt/decrypt up to 4KB of data.
		- they, by default, rotate about once a year. for AWS-managed keys, this can't be turned off. for customer-managed keys, it can be.
		- they can have aliases
	- **Data Encryption Keys (DEKs)** can be used on >4KB of data. they aren't stored- you'll receive a plaintext and ciphertext (encrypted with the KMS key you created it with) version, and you'll need to provide the ciphertext version to KMS in future of decryption.
		- generally, you encrypt some data with the plaintext key, then discard it, then store the encrypted key along with the data
- keys have policies which state which [[AWS/account]]s can manage them