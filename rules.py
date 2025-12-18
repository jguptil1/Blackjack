# rules.py
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class SplitPairRule(Enum):
    SAME_RANK = "same_rank"     # e.g., K+K only, J+J only
    SAME_VALUE = "same_value"   # e.g., J+K allowed (both 10-value)


@dataclass(frozen=True)
class Rules:
    # Shoe / dealing
    num_decks: int = 1

    # Dealer behavior
    dealer_hits_soft_17: bool = True  # H17 if True, S17 if False

    # Payouts (as multipliers on the bet)
    blackjack_payout: float = 1.5     # 3:2 is 1.5, 6:5 is 1.2
    regular_win_payout: float = 1.0   # normal win pays 1:1

    # Splitting
    allow_split: bool = True
    max_hands: int = 4                # common: up to 4 hands total
    split_pair_rule: SplitPairRule = SplitPairRule.SAME_RANK
    allow_resplit: bool = True
    allow_resplit_aces: bool = False
    hit_split_aces_allowed: bool = False
    blackjack_after_split_counts_as_blackjack: bool = False

    # Doubling
    allow_double: bool = True
    s: bool = True  # DAS

    # Surrender (optional)
    allow_surrender: bool = False

    # Bets (optional)
    min_bet: int = 1
    max_bet: Optional[int] = None

    # ---------- Policy helpers ----------
    def dealer_should_hit(self, hand_total: int, is_soft: bool) -> bool:
        """Given dealer's best total and whether it's soft, decide hit/stand."""
        if hand_total < 17:
            return True
        if hand_total > 17:
            return False
        # hand_total == 17
        return self.dealer_hits_soft_17 and is_soft

    def can_create_new_hand_via_split(self, current_hand_count: int) -> bool:
        """Splitting creates +1 hand; ensure we don't exceed max_hands."""
        return self.allow_split and (current_hand_count + 1) <= self.max_hands
