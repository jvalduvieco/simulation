from openfisca_barcelona import BarcelonaTaxBenefitSystem
from openfisca_core.simulations import Simulation


class Simulator:
    def __init__(self):
        self.tax_benefit_system = BarcelonaTaxBenefitSystem()

    def simulate(self, variable_name, period, simulation_data):
        simulation = Simulation(tax_benefit_system=self.tax_benefit_system,
                                simulation_json=simulation_data.to_openfisca_dict(period=period))
        result = simulation.calculate(variable_name, period=period)
        return result
