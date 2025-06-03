- ```
  Please summarize the attached materials into Logseq notes. These notes are written in a Markdown format, as bullet-point outlines. Each note has a title. Notes can link to other notes by using a Wiki-link syntax [[like this]]. Each note has a YAML frontmatter section inside a fence of triple dashes (`---`), which can include `tags` of categories the notes is about, and `aliases` the note can also be referred to by. You can use LaTeX syntax for math formulas when needed.
  
  Here are some examples of good notes:
  
  <example>
  ---
  tags: security
  ---
  
  # MFA
  
  - **multi-factor authenticaion** is a way to secure access to a resource more robustly than a simple name/password.
  - a **factor** is a piece of evidence which proves your identity. you can achieve greater security by combining multiple factors, such as:
  	- **knowledge:** something you know. usernames, passwords, security questions
  	- **possession:** something you have. MFA device, phone, ID card
  	- **inherent:** something you are. fingerprint, face, iris.
  	- **location:** somewhere you are. either physically, or a network.
  </example>
  
  <example>
  ---
  tags: systems thinking, systems engineering
  alias: complex system
  ---
  
  # complex systems
  
  - a complex [[system]] is a combination of systems that behave independently of their
    components.
  	- > A complex system is a system in which there are non-trivial relationships between cause and effect: each effect may be due to multiple causes; each cause may contribute to multiple effects; causes and effects may be related as feedback loops, both positive and negative; and cause-effect chains are cyclic and highly entangled rather than linear and separable
  	  — [[INCOSE]] Systems Engineering and System Definitions
  </example>
  
  <example>
  ---
  tags: Buddhism, theology, mindfulness
  ---
  
  # Satipatthana Sutta
  
  - suggests the **four foundations of mindfulness** as the way to overcome suffering and grief:
  	- contemplating the body in the body
  	- contemplating feelings in feelings
  	- contemplating consciousness in consciousness
  	- contemplating mental objects in mental objects
  	- these have an interesting recursive/self-referential structure!
  - # 1. Contemplation of the Body
  	- begins with mindfulness of breathing
  	- then, to mindfulness of the postures of the body
  	- then, to mindfulness with clear comprehension
  	- next, to reflection on the body and its anatomical parts as base objects:
  		- > Just as if there were a double-mouthed provision bag full of various kinds of grain such as hill paddy, paddy, green gram, cow-peas, sesamum, and husked rice, and a man with sound eyes, having opened that bag, were to take stock of the contents thus: "This is hill paddy, this is paddy, this is green gram, this is cow-pea, this is sesamum, this is husked rice." Just so, monks, a monk reflects on this very body enveloped by the skin and full of manifold impurity, from the soles up, and from the top of the head-hairs down, thinking thus: "There are in this body hair of the head, hair of the body, nails, teeth, skin, flesh, sinews, bones, marrow, kidney, heart, liver, midriff, spleen, lungs, intestines, mesentery, gorge, feces, bile, phlegm, pus, blood, sweat, fat, tears, grease, saliva, nasal mucus, synovial fluid, urine."
  		- might this be the origin of [[body scan]] meditation?
  		- cultivate an attitude of [[non-attachment]] to each of these parts
  	- next, to contemplation of the material elements in the body
  		- > And further, monks, a monk reflects on this very body, however it be placed or disposed, by way of the material elements: "There are in this body the element of earth, the element of water, the element of fire, the element of wind."
  		  Just as if, monks, a clever cow-butcher or his apprentice, having slaughtered a cow and divided it into portions, should be sitting at the junction of four high roads, in the same way, a monk reflects on this very body, as it is placed or disposed, by way of the material elements: "There are in this body the elements of earth, water, fire, and wind."
  		- reflect on: how each of these elements is empty of self. how each is changing and impermanent. how each is not truly owned or controlled by us. how there is no essential distinction between the element in the body, and the element outside the body. how the body is constantly reliant on a supply of elements from outside.
  </example>
  
  <example>
  ---
  tags: engineering, systems engineering, systems thinking
  ---
  
  # system
  
  - per [[INCOSE]]:
  	- > A system is a construct or collection of different elements that together produce results not obtainable by the elements alone.
  - per the DOD:
  	- > A system is an aggregation of system elements and enabling system elements to achieve a given purpose or provide a needed capability.
  - common characteristics of systems:
  	- a system is something made of integrated parts, with interfaces, boundaries, and relationships as key parts of the system
  	- a system is likely a team effort, probably even multi-team!
  	- a system generally has some defined purpose or capabilities
  	- a system can help us conceptualize and deal with complexity
  - we could think of something as simple as a stapler as a system. it has various parts that need to work together. but it's not very *interesting*- staplers are rather simple! we'd find the system perspective much more illuminating with a more complex system, like a research facility, or a battleship, or an ecosystem.
  - concepts we might think of:
  	- [[stocks, flows, and variables]]
  	- [[holism]]
  	- internal and external components
  	- [[boundary conditions]]
  	- inputs and outputs
  	- open or closed systems
  	- whole vs. parts
  	- [[feedback loops]]
  	- [[homeostasis]], [[self-regulation]], [[autopoiesis]], [[equifinality]]
  - a system is a perspective! it's a conceptual lens we apply to help us understand the world.
  - there can be both physical and conceptual systems, or physical and conceptual components of a given system. *meaning* is part of any sociotechnical system!
  - systems can be closed or open. [[entropy]], in closed systems, increases. but most of the systems we think about are open. so they are able to decrease entropy locally, by increasing it elsewhere outside the system
  - systems can occur in nature! a living body is a system.
  - systems thinking is inherently [[holistic]], since we think of the system as having something to it above and beyond the individual components.
  - systems are applicable in many disciplines. they tie in to [[ecology]], [[general systems theory]], 
    [[cybernetics]], [[systems engineering]], [[sociology]], and more.
  - a typology of systems, from INCOSE:
  	- a **physical system** is made out of matter and energy.
  	- a **conceptual system** are made out of information. they're arrangements that exhibit meaning which the constituent parts do not.
  	- a **closed system** is completely isolated from its environment. (in some terminologies, this is an **isolated system**, and a closed system is one that only exchanges energy)
  	- an **open system** can exchange [[information]], energy, or matter with the external environment
  	- a **natural system** occurs without human intervention
  	- an **artificial system** was created by humans
  	- a **hybrid system** has both natural and artificial elements
  	- an **engineered system** is a system created through [[systems engineering]]
  	- a **viable system** is an open system that, within certain environmental limits, can sustain itself in the face of threats and maintain [[homeostasis]]
  	- a **self-replicating system** is an open system that can reproduce itself.
  	- a [[complex system]] has non-trivial relationships between cause and effect. they're not fully knowable or deterministic.
  	- An **anticipatory system** has a model of itself and its environment and a decisionmaking system, allowing it to predict and adjust to environment change
  </example>
  
  <example>
  ---
  tags: stats, Bayes, classification
  ---
  
  # Bayes classifier
  
  - a classifier that uses [[Bayes' theorem]]. it assigns the class prediction to the class with the highest conditional probability, like so:
  	- $p_k(x) = \dfrac{\pi_k \cdot f_k(x)}{\sum_{l=1}^k{\pi_l \cdot f_l(x)}}$
  		- where $\pi_k$ is the [[prior]] estimate that the item belongs to class $k$, and $f_k(x)$ is the [[density function]] for class $k$, or likelihood
  	- stated differently, $C^\text{Bayes}(x) = \underset{r \in \{1,2,\dots, K\}}{\operatorname{argmax}} \operatorname{P}(Y=r \mid X=x)$
  - this classifier has the lowest theoretical misclassification rate.
  - but to use this in practice, we need to know $f_k(x)$! in reality, we usually don't.
  	- so, the Bayes classifier becomes the seed for a whole class of [[generative model]]s that plug in different functions for $f_k(x)$. [[linear discriminant analysis]], [[quadratic discriminant analysis]], and [[Naive Bayes]] all do this! (with different assumptions.)
  </example>
  
  Now that you've seen these examples, please summarize the attached files into a similar set of notes. Here are some rules to follow:
   - Keep it to between 1 and 5 notes, using only as many as you need to capture the content clearly, accurately, and succinctly.
   - Create only one note per topic. For example:
      - Don't create a notes titled "Topic X" and a separate note titled "Introduction to Topic X" or "Techniques for Topic X". Instead, create one note for "Topic X", containing all relevant info.
      - Don't create a note called "Common Algorithm Complexities". Instead, place that information either in the "Algorithm Complexities" note, or spread amongst the specific notes for the algorithms in question.
      - Don't create a note about a general or vague topic. Your note topics should be as specific as a Wikipedia article title.
  ```
-