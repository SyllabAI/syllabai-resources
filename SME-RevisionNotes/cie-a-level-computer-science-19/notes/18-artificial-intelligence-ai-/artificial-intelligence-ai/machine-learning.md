---
note_id: "rn_VZdHGM2VDbnV4xPN"
title: "Machine Learning"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/18-artificial-intelligence-ai-/artificial-intelligence-ai/machine-learning
path: 18-artificial-intelligence-ai-/artificial-intelligence-ai/machine-learning
updated_at: "2025-06-04T08:34:59.818Z"
spec_point_ids: ["spcpt_bY2pBD8YBHs9jWRZ", "spcpt_mGZdmv3QdMBSsgXD", "spcpt_PJ3XV294tnSqSBV3"]
spec_point_codes: []
guided_study: false
---

# Machine Learning

## Neural networks & deep learning

> **Spec point** — `spcpt_bY2pBD8YBHs9jWRZ`

## Neural networks & deep learning

### What is machine learning (ML)?

- Machine learning is **a type of artificial intelligence (AI)** that allows computers to:

  - **Learn patterns from data**
  - Improve performance **without being explicitly programmed**
- Instead of following fixed rules, machine learning systems:

  - **Analyse **large amounts of data
  - **Identify **patterns or trends
  - **Make **predictions or decisions based on that data
- ML is used in: spam filters, voice assistants, recommendation systems, fraud detection

### What are artificial neural networks (ANNs)?

- Artificial neural networks (ANNs) are **algorithms **inspired by the structure of the **human brain**

  - A neural network is made up of **layers of nodes (neurons)** connected by **weighted links**
  - Each neuron receives input, processes it, and passes the result to the next layer
  - The network **adjusts the weights** based on errors in output (using algorithms like backpropagation)

#### How ANNs help machine learning

- ANNs are powerful because they:

  - Automatically **learn from experience**, even with complex or unstructured data
  - Improve their accuracy with **more data and training**
  - Can solve problems that are **too complex for rule-based programming**
- Examples: handwriting recognition, speech recognition, image classification, language translation

### Deep learning (DL)

- Deep learning is a **subfield of machine learning** that uses **deep (multi-layered) neural networks**

  - The more layers a network has, the more complex patterns it can learn
  - Especially effective at learning **abstract features** in images, text, audio, and video
- Example: facial recognition apps learn features like eyes, noses, and then full faces through many layers

### Reinforcement learning (RL)

- Reinforcement learning is another type of machine learning where an **agent learns by interacting with an environment**

  - It **receives rewards** for good actions and **penalties** for poor actions
  - Over time, the agent learns an **optimal strategy** (called a *policy*) to maximise rewards
- Used in: robotics, self-driving cars, game-playing AI (like AlphaGo), industrial automation

### Summary: why use these methods?

| **Method** | **What it does** | **Why use it** |
|---|---|---|
| **Machine Learning** | Learns from labelled data | Automates decisions with high accuracy |
| **Artificial Neural Network** | Mimics human brain to recognise complex patterns | Excellent for handling messy, high-dimensional data |
| **Deep Learning** | Uses many neural layers to extract features | Performs well with images, language, sound |
| **Reinforcement Learning** | Learns by trial and error with feedback | Useful where there's no labelled data, only success/failure |

## Categories of machine learning

> **Spec point** — `spcpt_mGZdmv3QdMBSsgXD`

## Categories of machine learning

- Machine learning algorithms are categorised based on **how they learn from data**
- The two main categories are:

### Supervised learning

- Supervised learning is when the algorithm is trained on a **labelled dataset**
- Meaning the **input data** has **known outputs** (answers)

  - The goal is to learn a function that maps inputs to the correct output
  - Once trained, the model can make predictions on **unseen data**
- Example:

  - Input: Email text
  - Output: Spam or Not Spam
  - The model learns from thousands of pre-labelled emails

#### Used for:

- **Classification** (e.g. face recognition, spam detection)
- **Regression** (e.g. predicting house prices)

### Unsupervised learning

- Unsupervised learning is when the algorithm is given **unlabelled data**, and it must **find patterns** or **groupings** on its own

  - There are no correct answers, the system explores the data structure
  - It identifies **clusters, trends, or anomalies** without any guidance
- Example:

  - Input: Customer purchase data
  - Output: Groups of customers with similar buying habits

#### Used for:

- **Clustering** (e.g. customer segmentation, social network analysis)
- **Dimensionality reduction** (e.g. simplifying complex data)

## Back propagation & regression

> **Spec point** — `spcpt_PJ3XV294tnSqSBV3`

## Back propagation & regression

### What is back propagation?

- Back propagation is a training method used in **artificial neural networks** to **improve accuracy** by adjusting the weights of connections
- It is a key part of the **supervised learning** process and works as follows:

1. **Forward pass**:

  1. Input data passes through the network layer by layer
  2. The network produces an **output** (a prediction)
2. **Error calculation**

  1. The output is compared to the **actual target** value
  2. The **difference** is called the **error**
3. **Backward pass**

  1. The error is **propagated backwards** through the network
  2. Each layer calculates its **contribution to the error**
4. **Weight adjustment**

  1. The weights of the connections are updated using an algorithm (e.g. **gradient descent**) to reduce future errors

#### Why use back propagation?

- Helps the neural network **learn from mistakes**
- Makes the model more **accurate over time**
- Allows multi-layer networks to **fine-tune all layers**, not just the output
- Common in: image recognition, speech recognition, language translation

### What is regression?

- Regression is a type of **supervised learning** used to predict **continuous values** (rather than categories)
- The aim is to **find the relationship** between input features and a numerical output

#### Types of regression:

| **Type** | **Description** |
|---|---|
| **Linear regression** | Predicts output using a straight-line relationship (y = mx + c) |
| **Multiple linear regression** | Uses **multiple input features** to predict one continuous output |
| **Logistic regression** | Predicts **binary outcomes** (e.g. yes/no), despite the name “regression” |

#### Example: linear regression

- Predicting house prices based on square footage:

  - Input: size of house
  - Output: estimated price
  - The model learns a line that best fits the data points

#### Why use regression methods?

- Useful for **forecasting**, **trend analysis**, and **risk prediction**
- Interpretable, often used in real-world problems like:

  - Business analytics
  - Finance
  - Healthcare

> **Worked Example**
> Supervised and unsupervised learning are two categories of machine learning.
> 
> Describe supervised learning and unsupervised learning.**[4]**
> 
> **Final answer:** **Answer**
> 
> **Supervised learning (Max 3 of 4)**
> 
> - Supervised learning allows data to be collected, or a data output produced, from the previous experience **[1 mark]**
> - In supervised learning, known input and associated outputs are given **OR** uses sample data with known outputs (in training) **OR** uses labelled input data **[1 mark]**
> - Able to predict future outcomes based on past data **[1 mark]**
> 
> **Unsupervised learning (Max 3 of 4)**
> 
> - Unsupervised machine learning helps all kinds of unknown patterns in data to be found **[1 mark]**
> - Unsupervised learning only requires input data to be given **[1 mark]**
> - Uses any data **OR** not trained on the right output **OR** uses unlabelled input data **[1 mark]**
