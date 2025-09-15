# MNIST Digit Classifier 🔢

A simple deep learning project using **TensorFlow/Keras** to classify handwritten digits (0–9) from the **MNIST dataset**.

---

## 📌 Features

* Loads and preprocesses the **MNIST dataset** (60,000 training and 10,000 test images).
* Builds a simple **feedforward neural network** with:

  * Flatten layer
  * Dense hidden layer (128 neurons, ReLU activation)
  * Dense output layer (10 neurons, softmax activation)
* Trains the model for **5 epochs**.
* Evaluates the model accuracy on the test dataset.
* Accepts a custom **user-provided image**, preprocesses it, and predicts the digit.

---

## 🛠 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

**requirements.txt**:

```
tensorflow
numpy
pillow
```

---

## 🚀 Usage

1. Clone this repository:

```bash
git clone https://github.com/NoobSaifii/mnist-digit-classifier.git
cd mnist-digit-classifier
```

2. Run the script:

```bash
python mnist_classifier.py
```

3. Provide an image file (must be a digit on white background):

```text
pls write image file name: my_digit.png
number in img is: 7
```

---

## 📂 Project Structure

```
mnist-digit-classifier/
│-- mnist_classifier.py     # Main script
│-- requirements.txt        # Dependencies
│-- README.md               # Documentation
```

---

## 📊 Example Output

```
Epoch 1/5
1875/1875 [==============================] - 2s 1ms/step - loss: 0.2639 - accuracy: 0.9240
...
Epoch 5/5
1875/1875 [==============================] - 2s 1ms/step - loss: 0.0872 - accuracy: 0.9732

313/313 [==============================] - 0s 1ms/step - loss: 0.0904 - accuracy: 0.9736
model acc is: 0.9736
```

---

## 📖 Dataset

The project uses the **MNIST Handwritten Digit dataset**, available via `keras.datasets.mnist`.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and share.
