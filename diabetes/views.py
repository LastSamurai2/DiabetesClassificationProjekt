from django.shortcuts import render
from .models import DiabetesData
from .forms import PatientData
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

def primary_view(request):
    print(request)
    if 'first_button' in request.POST:
        form = PatientData(request.POST)
        if form.is_valid():
            pregnancies = form.cleaned_data['pregnancies']
            glucose = form.cleaned_data['glucose']
            blood_preasure = form.cleaned_data['blood_preasure']
            skin_thickness = form.cleaned_data['skin_thickness']
            insulin = form.cleaned_data['insulin']
            bmi = form.cleaned_data['bmi']
            diabetes_pedigree_function = form.cleaned_data['diabetes_pedigree_function']
            age = form.cleaned_data['age']


            data = DiabetesData.objects.all().values()
            df = pd.DataFrame(data)
            id_colum = df['id']
            target_column = df['outcome']

            df_to_algorithm = df.loc[:, df.columns != 'outcome']
            df_to_algorithm = df_to_algorithm.loc[:, df_to_algorithm.columns != 'id']

            # print(df_to_algorithm.describe())
            X = df_to_algorithm
            y = target_column

            X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                                test_size=0.30,
                                                                random_state=40)
            print(X_train.shape)
            print(X_test.shape)

            # one hot encode outputs
            y_train = to_categorical(y_train)
            y_test = to_categorical(y_test)

            count_classes = y_test.shape[1]
            print(count_classes)

            model = Sequential()
            model.add(Dense(500, activation='relu', input_dim=8))
            model.add(Dense(100, activation='relu'))
            model.add(Dense(50, activation='relu'))
            model.add(Dense(2, activation='softmax'))

            # Compile the model
            model.compile(optimizer='adam',
                          loss='categorical_crossentropy',
                          metrics=['accuracy'])

            model.fit(X_train, y_train, epochs=100)

            scores2 = model.evaluate(X_test, y_test, verbose=0)
            print('Accuracy on test data: {}% \n Error on test data: {}'.format(
                scores2[1], 1 - scores2[1]))

            new_row_id = len(X_test.index) + 1
            new_row_data = pd.DataFrame({"pregnancies": pregnancies, "glucose": glucose,
                            "blood_preasure": blood_preasure,
                            "skin_thickness": skin_thickness,
                            "insulin": insulin, "bmi": bmi,
                            "diabetes_pedigree_function": diabetes_pedigree_function,
                            "age": age}, index=[1000])
            print(X_test.shape)

            X_test = X_test.append(new_row_data)
            print(X_test)
            print(new_row_data)

            pred_test = model.predict(X_test)
            print("pred_test",pred_test)
            print(classification_report(y_test, pred_test))

            y_predict = model.predict(
                [[1, 148, 72, 35, 79.799, 33.6, 0.627, 50]])
            print(y_predict)
            print("czy działa?")
            if y_predict == 1:
                print("Diabetic")
            else:
                print("Non Diabetic")

            return render(request, "index.html")

    form = PatientData()
    context = {

    }

    return render(request, "index.html", {'form':form})
