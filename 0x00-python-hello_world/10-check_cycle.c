#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: The linked list to check
 *
 * Return: 0 if no cycle is present and 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *current_node = malloc(sizeof(listint_t));

	while (current_node->next != NULL)
	{
		if (current_node->next == head)
		{
			free(current_node);
			return (1);
		}

		current_node = current_node->next;
	}

	free(current_node);
	return (0);
}
