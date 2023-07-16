import matplotlib.pyplot as plt
import numpy as np
import locale
import calendar

# Set the locale for formatting currency values
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Set the plot style
plt.style.use('_mpl-gallery')

# Creating in/out plot


def create_in_out_plot():
    # Non-formatted data
    income = [
        "R$ 4002.65", "R$ 4176.65", "R$ 4567.22",
        "R$ 4730.80", "R$ 4874.51", "R$ 5018.22",
        "R$ 5231.94", "R$ 5445.65", 'R$ 5735.08'
    ]
    outcome = [
        "R$ 9,276.50", "R$ 8,651.50", "R$ 8,761.50",
        "R$ 8,721.50", 	"R$ 8,951.50", " R$ 8,771.50",
        "R$ 8,651.50", 	"R$ 8,651.50", "R$ 8,951.50",

    ]

    # Format the data as float values
    formatted_income = [
        float(
            value.replace('R$', '').replace(',', '').replace(' ', '')
        ) for value in income
    ]
    formatted_outcome = [
        float(
            value.replace('R$', '').replace(',', '').replace(' ', '')
        ) for value in outcome
    ]

    # Make data
    months = calendar.month_abbr[1:10]
    x = np.arange(len(months))

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Create the bar plots
    ax.bar(
        x - 0.2, formatted_income, width=0.4, label='Entrada', color='green'
    )
    ax.bar(
        x + 0.2, formatted_outcome, width=0.4, label='Saída', color='red'
    )

    # Set the x-axis labels as months
    ax.set_xticks(x)
    ax.set_xticklabels(months)

    # Format y-axis labels as currency
    ax.set_yticklabels([
        locale.currency(tick, grouping=True) for tick in ax.get_yticks()
    ])

    # Add data labels above each column
    for i, v in enumerate(formatted_income):
        color = 'red' if v < 0 else 'black'
        ax.text(i - 0.2, v + 10, locale.currency(v, grouping=True),
                ha='center',
                fontsize=9,
                color=color)
    for i, v in enumerate(formatted_outcome):
        ax.text(i + 0.2, v + 10, locale.currency(v, grouping=True),
                ha='center',
                fontsize=9)

    # Add a legend
    ax.legend()

    # Adjust the plot view to zoom out
    plt.subplots_adjust(bottom=0.15, left=0.15)
    plt.show()

# Creating cash flow plot


def create_cash_flow_plot():
    # Non-formatted data
    cash_flow = [
        '-R$ 152.35', 'R$ 407.90', 'R$ 717.22',
        'R$ 920.80', 'R$ 1,134.51', 'R$ 1,158.22',
        'R$ 1,491.94', 'R$ 1,705.65', 'R$ 1,995.08'
    ]

    cash_flow_need = [
        'R$ 4155', 'R$ 3768.75', 'R$ 3850',
        'R$ 3810', 'R$ 3740', 'R$ 3860',
        'R$ 3740', 'R$ 3,740.00', 'R$ 3,740.00'
    ]

    # Format the data as float values
    formatted_cash_flow = [
        float(
            value.replace('R$', '').replace(',', '').replace(' ', '')
        ) for value in cash_flow
    ]
    formatted_cash_flow_need = [
        float(
            value.replace('R$', '').replace(',', '').replace(' ', '')
        ) for value in cash_flow_need
    ]

    # Make data
    months = calendar.month_abbr[1:10]
    x = np.arange(len(months))

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Create the bar plots
    ax.bar(
        x - 0.2, formatted_cash_flow,
        width=0.4, label='Capital de Giro')
    ax.bar(
        x + 0.2, formatted_cash_flow_need,
        width=0.4, label='Necessidade de Capital de Giro'
    )

    # Set the x-axis labels as months
    ax.set_xticks(x)
    ax.set_xticklabels(months)

    # Format y-axis labels as currency
    ax.set_yticklabels([
        locale.currency(tick, grouping=True) for tick in ax.get_yticks()
    ])

    # Add data labels above each column
    for i, v in enumerate(formatted_cash_flow):
        color = 'red' if v < 0 else 'black'
        ax.text(i - 0.2, v + 10, locale.currency(v, grouping=True),
                ha='center',
                fontsize=9,
                color=color)
    for i, v in enumerate(formatted_cash_flow_need):
        ax.text(i + 0.2, v + 10, locale.currency(v, grouping=True),
                ha='center',
                fontsize=9)

    # Add a legend
    ax.legend()

    # Adjust the plot view to zoom out
    plt.subplots_adjust(bottom=0.15, left=0.15)

    plt.show()


if __name__ == "__main__":
    create_in_out_plot()
    create_cash_flow_plot()
