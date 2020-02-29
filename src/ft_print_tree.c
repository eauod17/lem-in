/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_tree.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: del-alj <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/02/17 08:47:40 by del-alj           #+#    #+#             */
/*   Updated: 2020/02/29 14:42:14 by del-alj          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_lem_in.h"

void	ft_print_tree(t_avl *tree, char c)
{
	if (tree == NULL)
		return ;
	ft_printf("|%s| - %c -> %d\n", tree->name, c, tree->height);
	ft_print_tree(tree->right, 'r');
	ft_print_tree(tree->left, 'l');
}
