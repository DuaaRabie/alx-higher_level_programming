#include "lists.h"

/**
 * check_cycle - check cycle lists
 * @list: pointer to the list to be checked
 * Return: 0 no cycle | 1 there is a cycle
 */
int check_cycle(listint_t *list)
{
	int j = 0, i = 1;
	listint_t *temp = list, *next, *array[200], *loop = NULL;

	if (list == NULL)
		return (0);

	array[0] = list;
	if (temp->next == temp)
		return (1);

	while (temp->next != loop)
	{
		j = 0;
		next = temp->next;
		temp = next;
		array[i] = temp;
		array[i + 1] = NULL;
		while (array[j])
		{
			if (temp->next == array[j])
				return (1);
			j++;
		}
		i++;
	}

	return (0);
}
