import matplotlib.pyplot as plt
import numpy as np



accuracies = [0.5842696629213483, 0.7311827956989247, 0.7435897435897436, 0.7386363636363636, 0.4823529411764706, 0.7297297297297297, 0.9365079365079365, 0.7529411764705882, 0.8795180722891566, 0.851063829787234, 0.9565217391304348, 0.85, 0.8223684210526315, 0.7634408602150538, 0.9021739130434783, 0.8842105263157894, 0.7604166666666666, 0.98989898989899, 0.9285714285714286, 0.797752808988764, 0.7790697674418605, 0.788235294117647, 0.5913978494623656, 0.8058252427184466, 0.8552631578947368, 0.6888888888888889, 0.782608695652174, 0.7297297297297297, 0.7204301075268817, 0.7857142857142857, 0.7215189873417721, 0.7027027027027027, 0.611764705882353, 0.8673469387755102, 0.8295454545454546, 0.547945205479452]

f1_scores = [0.5841956303594235, 0.7257526774351023, 0.7374027272078246, 0.7267234200864161, 0.4989873652917131, 0.7180512101269465, 0.9371508637686996, 0.7326203208556151, 0.8786507936507936, 0.8433907804851365, 0.9535066030322198, 0.8426778818679984, 0.8363003703450711, 0.7539789862305075, 0.9024666467542811, 0.8907608679046972, 0.7556647479737405, 0.98989898989899, 0.9281531531531533, 0.7843767754441449, 0.7620180845724324, 0.7833635898152028, 0.5344396344396344, 0.819655874175243, 0.8531338563522471, 0.6967457829526795, 0.7860183664781365, 0.7024654208158045, 0.719914249224594, 0.7852273525897814, 0.7200407085464557, 0.6679505016571086, 0.5432728484240242, 0.8692439096850862, 0.8173094834857704, 0.48785190176699605]


plt.figure(3)
plt.suptitle('LSTM performance for Exp. 1', fontsize=20)
plt.xlabel('users', fontsize=14)
plt.ylabel('scores', fontsize=14)
plt.plot(accuracies, label='accuracy')
plt.plot(f1_scores, label='f1 score')
# plt.xticks(np.arange(0, 37, 5))
plt.legend(loc="upper right")
plt.savefig("exp1.png", dpi=300)