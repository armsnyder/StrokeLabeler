import unittest
import StrokeHmm


class TestViterbi(unittest.TestCase):

    def test_rain(self):
        hmm = StrokeHmm.HMM(['rain', 'clear'], ['umbrella'], {'umbrella': StrokeHmm.DISCRETE}, {'umbrella': 2})
        prior = {
            'rain': 0.5,
            'clear': 0.5
        }
        transition = {
            'rain': {
                'rain': 0.7,
                'clear': 0.3
            },
            'clear': {
                'rain': 0.3,
                'clear': 0.7
            }
        }
        emission = {
            'rain': {
                'umbrella': [0.9, 0.1]
            },
            'clear': {
                'umbrella': [0.2, 0.8]
            }
        }
        hmm.emissions = emission
        hmm.priors = prior
        hmm.transitions = transition
        self.assertEqual(['rain', 'rain', 'rain'], hmm.label([{'umbrella': 0}, {'umbrella': 0}, {'umbrella': 0}]))

    def test_rain_more(self):
        hmm = StrokeHmm.HMM(['rain', 'clear'], ['umbrella'], {'umbrella': StrokeHmm.DISCRETE}, {'umbrella': 2})
        prior = {
            'rain': 0.5,
            'clear': 0.5
        }
        transition = {
            'rain': {
                'rain': 0.7,
                'clear': 0.3
            },
            'clear': {
                'rain': 0.3,
                'clear': 0.7
            }
        }
        emission = {
            'rain': {
                'umbrella': [0.9, 0.1]
            },
            'clear': {
                'umbrella': [0.2, 0.8]
            }
        }
        hmm.emissions = emission
        hmm.priors = prior
        hmm.transitions = transition
        self.assertEqual(['clear', 'clear', 'rain'], hmm.label([{'umbrella': 1}, {'umbrella': 1}, {'umbrella': 0}]))

    def test_wikipedia(self):
        states = ('Healthy', 'Fever')
        observations = ('normal', 'cold', 'dizzy')
        start_probability = {'Healthy': 0.6, 'Fever': 0.4}
        transition_probability = {
           'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
           'Fever': {'Healthy': 0.4, 'Fever': 0.6}
           }
        emission_probability = {
           'Healthy': {'normal': [0.5, 0.5], 'cold': [0.4, 0.6], 'dizzy': [0.1, 0.9]},
           'Fever': {'normal': [0.1, 0.9], 'cold': [0.3, 0.7], 'dizzy': [0.6, 0.4]}
           }
        hmm = StrokeHmm.HMM(states, observations, {
            'normal': StrokeHmm.DISCRETE,
            'cold': StrokeHmm.DISCRETE,
            'dizzy': StrokeHmm.DISCRETE
        }, {
            'normal': 2,
            'cold': 2,
            'dizzy': 2})
        hmm.emissions = emission_probability
        hmm.priors = start_probability
        hmm.transitions = transition_probability
        self.assertEqual(['Healthy', 'Healthy', 'Fever'], hmm.label([{'normal': 0, 'cold': 1, 'dizzy': 1},
                                                                     {'normal': 1, 'cold': 0, 'dizzy': 1},
                                                                     {'normal': 1, 'cold': 1, 'dizzy': 0}]))

class TestConfusion(unittest.TestCase):
    def test_confusion(self):
        self.assertEqual({'drawing': {'drawing': 0, 'text': 3}, 'text': {'drawing': 3, 'text': 2}},
                         StrokeHmm.confusion(['drawing', 'text', 'text', 'text', 'drawing', 'drawing', 'text', 'text'],
                                             ['text', 'drawing', 'drawing', 'drawing', 'text', 'text', 'text', 'text']))
    def test_featurefy(self):
        test_labeler = StrokeHmm.StrokeLabeler()
        test_labeler.featureTest("trainingFiles/4242_2.9.1.labeled.xml")

    # def test_labeler(self):
    #     test_stroke = StrokeHmm.StrokeLabeler()
    #     # test_stroke.featureTest("trainingFiles/4242_2.9.1.labeled.xml")
    #     stroke_labels = test_stroke.loadLabeledFile("trainingFiles/0128_6.1.1.labeled.xml")
    #     print stroke_labels[0][3].strokeId
    #     print stroke_labels[0][3].length()
    #     print stroke_labels[0][3].sumOfCurvature(abs)
    #     print stroke_labels[0][3].distFromLeft()
    #     print stroke_labels[0][3].strokeSpeed()
    #
    #     length_tol = 100
    #     curvature_tol = 0.2
    #     distfromLeft_tol = 200
    #     strokeSpeed_tol = 0.5
    #
    #     test_stroke2 = StrokeHmm.StrokeLabeler()
    #
    #     test_stroke_bunch = test_stroke2.loadStrokeFile("trainingFiles/4242_2.7.1.labeled.xml")
    #
    #     for ind_stroke in test_stroke_bunch:
    #         lengthtest = abs(ind_stroke.length() - stroke_labels[0][3].length())
    #         curvetest = abs(ind_stroke.sumOfCurvature(abs) - stroke_labels[0][3].sumOfCurvature(abs))
    #         distTest = abs(ind_stroke.distFromLeft() - stroke_labels[0][3].distFromLeft())
    #         # print ind_stroke.strokeId
    #
    #         if (lengthtest < 40) and (curvetest < 40) and (distTest < 200):
    #             print "it's a b"
    #             print ind_stroke.strokeId
    #             print lengthtest, curvetest, distTest
    #
    #
    #     print "***************** NEW FILE ************"
    #     test_stroke_bunch = test_stroke2.loadStrokeFile("trainingFiles/0128_6.1.1.labeled.xml")
    #
    #     for ind_stroke in test_stroke_bunch:
    #         lengthtest = abs(ind_stroke.length() - stroke_labels[0][3].length())
    #         curvetest = abs(ind_stroke.sumOfCurvature(abs) - stroke_labels[0][3].sumOfCurvature(abs))
    #         distTest = abs(ind_stroke.distFromLeft() - stroke_labels[0][3].distFromLeft())
    #         # print ind_stroke.strokeId
    #         # print lengthtest, curvetest, distTest
    #
    #         if (lengthtest < 80) and (curvetest < 0.2) and (distTest < 200):
    #             print "it's a b"
    #             print ind_stroke.strokeId
    #             print lengthtest, curvetest, distTest






        test_labels = test_stroke.loadLabeledFile("trainingFiles/4242_2.9.1.labeled.xml")



        # for stork in stroke_labels:
        #     print " "
        #     print stork.substrokeIds[0]
        #     print "Length is", stork.length()
        #     print "Curvature is", stroke_labels[i].sumOfCurvature(abs)
        #     print "Speed is", stroke_labels[i].strokeSpeed()


