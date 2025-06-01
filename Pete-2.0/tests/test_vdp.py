import unittest
from src.vdp import InputHandler, SeedTriggerEngine, Thought, FieldResonanceEvaluator, ThoughtMemoryManager, DriftCoreEngine

class TestVDP(unittest.TestCase):
    def setUp(self):
        self.input_handler = InputHandler()
        self.trigger_engine = SeedTriggerEngine()
        self.field_evaluator = FieldResonanceEvaluator()
        self.memory_manager = ThoughtMemoryManager()
        self.drift_engine = DriftCoreEngine(self.field_evaluator, self.memory_manager)

    def test_drift_thought(self):
        raw_input = "I always wonder why we exist"
        signal = self.input_handler.receive_input(raw_input)
        thought = self.trigger_engine.trigger_seed(signal)
        result = self.drift_engine.drift_thought(thought)
        self.assertIn("Thought drifted to field", result)

if __name__ == '__main__':
    unittest.main()