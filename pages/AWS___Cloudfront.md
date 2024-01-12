tags:: aws, cloud

- Tidbits:
	- Cloudfront supports TLS, and S3 does not. This means we may want CloudFront in front of an [[AWS/S3]] bucket even if we don't need CDN, because S3 doesn't support TLS.