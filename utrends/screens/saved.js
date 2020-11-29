import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export function SavedScreen() {
    return (
      <View style={styles.container}>
        <Text>Saved stories</Text>
      </View>
    );
  }

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  }
});
