# 🚢 Titanic Data Analysis & Visualization

<p align="center">
  <img src="assets/titanic_hero.png" alt="Titanic Data Analysis" width="100%">
</p>

<p align="center">
  <b>Interactive Titanic Dataset Analysis & Visualization using Streamlit</b><br>
  Data Cleaning • Exploratory Data Analysis • Visualization • Correlation Analysis
</p>

---

## 📌 Project Overview

This project is an **interactive Titanic Data Analysis & Visualization web application** built using **Python and Streamlit**.

The application loads the Titanic dataset, performs basic data cleaning, displays the cleaned dataset, and provides multiple visualizations to understand passenger survival patterns based on **survival status, gender, passenger class, age, and numerical correlations**.

The main goal of this project is to understand how **Exploratory Data Analysis (EDA)** and visualization can be used to discover meaningful patterns in a real-world dataset.

---

## 🎯 Project Objectives

* Load and explore the Titanic dataset
* Perform basic data cleaning
* Remove missing values
* Display raw and cleaned datasets
* Analyze survival counts
* Analyze survival based on gender
* Analyze survival based on passenger class
* Understand age distribution
* Generate a numerical correlation matrix
* Build an interactive Streamlit dashboard
* Present analysis in a simple and visual format

---

## 🛠️ Technologies Used

| Technology    | Purpose                          |
| ------------- | -------------------------------- |
| 🐍 Python     | Programming Language             |
| 🎈 Streamlit  | Interactive Web Application      |
| 🐼 Pandas     | Data Loading & Data Manipulation |
| 📊 Matplotlib | Data Visualization               |
| 📈 Seaborn    | Statistical Visualization        |
| 📁 CSV        | Dataset Storage                  |

---

## 📂 Project Structure

```text
Titanic_Streamlit/
│
├── app.py
├── titanic1.csv
├── README.md
│
└── assets/
    └── titanic_hero.png
```

---

## 🔄 Project Workflow

```text
Titanic Dataset
       ↓
Load CSV File
       ↓
Data Exploration
       ↓
Data Cleaning
       ↓
Remove Missing Values
       ↓
Data Visualization
       ↓
Survival Analysis
       ↓
Correlation Analysis
       ↓
Streamlit Dashboard
```

---

# 📊 Analysis & Visualizations

## 1️⃣ Dataset Display

The application loads the Titanic dataset using Pandas and displays the complete dataset using Streamlit.

```python
a = pd.read_csv(csv_path)

st.dataframe(a)
```

This allows users to interactively view the dataset directly in the web application.

---

## 2️⃣ Data Cleaning

Missing values are removed using:

```python
b = a.dropna()
```

The cleaned dataset is then displayed separately.

```python
st.subheader("Cleaned Data")
st.dataframe(b)
```

This provides a simple comparison between the original and cleaned dataset.

---

## 3️⃣ Survival Count

A count plot is used to visualize the number of passengers who:

* ❌ Did not survive
* ✅ Survived

```python
sns.countplot(x="Survived", data=a, ax=ax1)
```

### Insight

The visualization helps understand the overall survival distribution of Titanic passengers.

---

## 4️⃣ Survival by Gender

A bar plot is used to analyze survival rates according to passenger gender.

```python
sns.barplot(
    x="Sex",
    y="Survived",
    data=a,
    ax=ax2
)
```

### Insight

This visualization helps identify differences in survival rates between male and female passengers.

---

## 5️⃣ Survival by Passenger Class

Passenger class is analyzed using:

```python
sns.barplot(
    x="Pclass",
    y="Survived",
    data=a,
    ax=ax3
)
```

The analysis compares survival rates among:

* First Class
* Second Class
* Third Class

### Insight

Passenger class can be examined as an important factor associated with survival outcomes.

---

## 6️⃣ Age Distribution

A histogram is used to understand the distribution of passenger ages.

```python
sns.histplot(
    data=a,
    x="Age",
    bins=20,
    ax=ax4
)
```

### Insight

The age distribution helps understand the demographic composition of passengers.

---

## 7️⃣ Correlation Matrix

A correlation matrix is created using numerical columns:

```python
corr = a.corr(numeric_only=True)
```

The result is visualized using a Seaborn heatmap.

```python
sns.heatmap(
    corr,
    annot=True,
    cmap="YlGnBu",
    linewidths=0.5,
    ax=ax5
)
```

### Insight

The correlation matrix helps identify the strength and direction of **linear relationships between numerical variables**.

> ⚠️ Correlation indicates association, not causation.

---

# 🎨 Streamlit Dashboard

The application provides an interactive web interface containing:

### 📋 Data Section

* Original Titanic dataset
* Cleaned Titanic dataset

### 📊 Visualization Section

* Survival Count
* Survival by Gender
* Survival by Passenger Class
* Age Distribution
* Correlation Matrix

---

# 🚀 How to Run the Project

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2. Open the Project Folder

```bash
cd Titanic_Streamlit
```

## 3. Install Required Libraries

```bash
pip install streamlit pandas matplotlib seaborn
```

## 4. Run the Streamlit Application

⚠️ **Important:** Streamlit applications should be started using `streamlit run`, not `python app.py`.

```bash
streamlit run app.py
```

## 5. Open in Browser

Streamlit will provide a local URL similar to:

```text
http://localhost:8501
```

Open this URL in your browser.

---

# 📦 Requirements

The project requires:

```text
Python 3.x
Streamlit
Pandas
Matplotlib
Seaborn
```

You can also create a `requirements.txt` file:

```text
streamlit
pandas
matplotlib
seaborn
```

Then install everything using:

```bash
pip install -r requirements.txt
```

---

# 💡 Key Learning Outcomes

Through this project, I practiced:

* Python programming
* Pandas DataFrame operations
* CSV data handling
* Missing-value handling
* Exploratory Data Analysis
* Data visualization
* Matplotlib
* Seaborn
* Correlation analysis
* Streamlit application development
* Building an interactive data-analysis dashboard

---

# 📈 Future Improvements

The project can be further enhanced by adding:

* 🔹 Interactive filters
* 🔹 Passenger-level prediction
* 🔹 Machine Learning survival prediction
* 🔹 Model accuracy comparison
* 🔹 Feature engineering
* 🔹 Interactive charts
* 🔹 Downloadable analysis reports
* 🔹 Deployment using Streamlit hosting

---

# 🏆 Project Highlights

| Feature                     | Status    |
| --------------------------- | --------- |
| Dataset Loading             | ✅         |
| Data Cleaning               | ✅         |
| Missing Value Handling      | ✅         |
| Survival Analysis           | ✅         |
| Gender Analysis             | ✅         |
| Passenger Class Analysis    | ✅         |
| Age Distribution            | ✅         |
| Correlation Analysis        | ✅         |
| Streamlit Dashboard         | ✅         |
| Interactive Filters         | 🔄 Future |
| Machine Learning Prediction | 🔄 Future |

---

# 👨‍💻 Author

**Manan**

Python • Machine Learning • Data Analysis • Power BI

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

<p align="center">
  <b>🚢 Titanic Data Analysis & Visualization</b><br>
  Built with Python 🐍 + Pandas 🐼 + Seaborn 📊 + Streamlit 🎈
</p>
