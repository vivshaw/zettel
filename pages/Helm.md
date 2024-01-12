tags:: distsys, kubernetes

- [Helm](https://helm.sh/), "the package manager for Kubernetes", is a tool to help mange the complexity of deploying a full app on k8s.
	- without Helm, you could write an indvidual YAML file for each and every service, then `kubectl apply` them all in the right order, providing the right secrets... Helm lets you *not* do that.
	- how do we edit something in app, and ensure that all parts are edited consistent to out change? how do we ensure when an app is sunset, we spin down all its parts? Helm helps with that.
	- Helm does this by letting you write config files with [[YAML]] and [[Go]] templates to specify exactly what the app needs
- think of [[Kubernetes]] as low-level- it is concerned with pods, and services, and volumes, but not what we built on them. Helm is about _apps_- the actual [[gestalt]] we conjure out of all that k8s YAML.
	- that's pretty [[sick]]!
- basic helm concepts
	- **chart**
		- a Helm chart is a collection of files with all the specifications for how to install an app
	- **release**
		- a release is a single installation of a Helm chart
	- **revision**
		- a versioned snapshot of a release
- templating:
	- you can template in values using [the Go template language](https://pkg.go.dev/text/template), and operate on those values with [functions and pipes](https://helm.sh/docs/chart_template_guide/functions_and_pipelines/)
	- you can use [named templates](https://helm.sh/docs/chart_template_guide/named_templates/) to keep it DRY
		- files starting with an `_` aren't converted into a Kubernetes YAML file. then do something like:
		  ```YAML
		  {{- define "mychart.labels" }}
		    labels:
		      generator: helm
		      date: {{ now | htmlDate }}
		  {{- end }}
		  ```
		- be aware you might need to fix the indentation with `indent`! that's a bit #jacked. #footguns
- chart hooks:
	- similar to Git hooks, can run commands at a specific point in the lifecycle
	- hooks available:
		- **pre-** / **post-install**
		- **pre-** / **post-upgrade**
		- **pre-** / **post-delete**
		- **pre-** / **post-delete**
	- you run commands _as Kubernetes objects_- define a [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) quite similar to a pod
	- you determine their order by setting a _weight_
	- the hook and the weight are defined in metadata, as annotations:
	  ```YAML
	    annotations:
	      # This is what defines this resource as a hook. Without this line, the
	      # job is considered part of the release.
	      "helm.sh/hook": post-install
	      "helm.sh/hook-weight": "-5"
	      "helm.sh/hook-delete-policy": hook-succeeded
	  ```
- [useful tips n' tricks from the official docs](https://helm.sh/docs/howto/charts_tips_and_tricks/)