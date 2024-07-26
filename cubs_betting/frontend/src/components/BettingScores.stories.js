import React from 'react';
import BettingScores from './BettingScores';

export default {
  title: 'Components/BettingScores',
  component: BettingScores,
};

const Template = (args) => <BettingScores {...args} />;

export const Default = Template.bind({});
Default.args = {
  // Add default props here
};
