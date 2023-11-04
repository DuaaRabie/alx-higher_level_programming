#include "lists.h"

/**
 * check_cycle - check cycle lists
 * @list: pointer to the list to be checked
 * Return: 0 no cycle | 1 there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list, *speed_temp;

	if (list == NULL || list->next == NULL)
		return (0);

	speed_temp = list->next;
	while (speed_temp && speed_temp->next)
	{
		if (speed_temp->next == temp)
			return (1);
		temp = temp->next;
		speed_temp = speed_temp->next->next;
	}

	return (0);
}
