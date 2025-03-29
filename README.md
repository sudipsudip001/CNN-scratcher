# CNN-scratcher

**CNNs** are one of the most revolutionary neural network feats. They were an improvement upon the previously existing *vanilla neural network* and performed better for **image classification** and **identification tasks** with comparatively fewer parameters and computations using cleverly designed architectures. 

> In this mini-project, I tried implementing a **CNN from scratch** to dive into the details of how things really work under the hood. 

The use of libraries like **PyTorch** and **TensorFlow** abstracts the underlying mechanisms and concepts of the actual operations. Though it makes it harder for you to improve your network if you don't know what you're doing, I have to say that my respect and appreciation for these libraries have increased **tenfold** simply because of how easy they make our lives. 

I was glad and surprised to encounter so many small details of CNNs that I *thought* I had understood well. Working on the network and crunching numbers really helps in understanding everything deeply, and you get a *'feel'* for the network. The whole process was challenging, but I think **limits exist for us to push past them and reach the next level.**

---

## Network Architecture

To talk about the network itself, we have two major layers, as in every CNN:

📌 **Feature Extraction Layer** (composed of a *Convolution layer* and a *Max-Pooling layer*)
📌 **Neural Network Layer**

There are **two convolutional layers**, each followed by **ReLU** and a **max-pooling layer**. 

- **First Convolutional Layer:**
  - Filter size: `(2, 1, 3, 3)` → *2 filters of depth 1, size 3×3*
  - Stride: **1**
  - Max-pooling stride: **2** (Halves input dimensions)

- **Second Convolutional Layer:**
  - Filter size: `(4, 2, 3, 3)` → *4 filters of depth 2, size 3×3*
  - Output size after max-pooling: `(4, 6, 6)`

The output is then **flattened** and passed to a neural network of two layers (*excluding the input layer*):
- **Layer 1:** 50 neurons
- **Layer 2:** 10 neurons

💡 *A tricky part in forward propagation was dealing with the depth of the convolutional filter in relation to the input it received.* 

For example:
```
Input: (1, 32, 32)
After convolving with (2, 1, 3, 3): Output = (2, 30, 30)
Formula: (input_size - filter_size + 2 * padding) / stride + 1
```
Similarly, for input `(2, 15, 15)`, after convolving with `(4, 2, 3, 3)`, we get a result of `(4, 12, 12)`. (*Note: The actual size would be (4, 13, 13), but I excluded one pixel to simplify the max-pooling operation.*)

---

## Backpropagation

✏️ **Using formulas was my go-to option for backpropagation.**

There is a slight variation in the **naming** of the operation performed:
> Though we name it *convolution*, it's actually a **cross-correlation operation** that we're applying. 

📌 *Convolution happens to be the cross-correlation operation performed after a 180-degree rotation.* However, for simplicity, I will continue referring to it as the **convolution operation**.

### Gradient Calculation:
- **Neural Network Part:** Straightforward and already well established.
- **Filter Gradient Calculation:**
  - Uses **convolution operation** between (input and gradient values).
  - For multiple convolutional filters: Uses **padded gradient values** and the **180-degree rotated filter**.
- **Max-Pooling Gradient:**
  - **Max-pooling:** Gradient calculated **only at the max value positions**.
  - **Average pooling:** Gradient distributed **equally**.
- **Activation Functions Gradient:** Simply the **derivative** of the function.

---

## The Struggle

🔴 **My problem:** While I could complete these operations correctly, I struggled to make the model actually **learn**. It simply wasn't learning to predict correctly. 

📌 *I had trouble training a single image to be classified correctly, making concrete progress difficult.*

---

## The Hard Truth

🚨 **Sadly, I just can't improve on this project any further at this time, so I have to abandon it.**

Though I have a detailed understanding of its inner mechanisms, I am **burnt out** and out of ideas at this moment. 

💭 *I would love to return to it later or maybe even start a new identical scratch project.*

This was supposed to be a **weekend project** but ended up taking **much longer** due to other commitments. 

Well, if I can stop my rambling, **that's it for now!**

⚡ **I can't commit to this project any further at the moment.**

