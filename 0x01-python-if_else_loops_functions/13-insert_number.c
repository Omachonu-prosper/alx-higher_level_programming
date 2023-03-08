#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_noode - inserts a number into a sorted singly linked list
 * @head: The head of the list
 * @number: The number to insert into the linked list
 *
 * Return: The address of the new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node;
	listint_t *previous_node;
	listint_t *insert_node;

	current_node = *head;
	previous_node = NULL;
	insert_node = malloc(sizeof(listint_t));
	if (insert_node == NULL)
		return (NULL);

	insert_node->n = number;

	while (current_node->next != NULL)
	{
		if (current_node->n > number)
		{
			previous_node->next = insert_node;
			insert_node->next = current_node;

			return insert_node;
		}

		previous_node = current_node;
		current_node = current_node->next;
	}

	return (NULL);
}
