import unittest
import StrokeHmm


class TestBasic(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

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
        self.assertEqual(['Healthy', 'Healthy', 'Fever'], hmm.label([{'umbrella': 1}, {'umbrella': 1}, {'umbrella': 0}]))