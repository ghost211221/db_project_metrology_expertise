export const SelectionsMixin = {
  data () {
    return {
      firstEl: '',
      secondEl: '',
      selectedRange: null,
      range: null,
      spanNum: 0,
      selectedId: ''
    }
  },
  methods: {
    onmousedown (event) {
      this.firstEl = event.target.className
      this.selectedId = event.target.id
    },
    onmouseup (event) {
      this.secondEl = event.target.className
      this.highlight()
      this.$emit('textSelected', window.getSelection().toString(), true)
    },
    getSelectedRange () {
      if (window.getSelection) {
        const sel = window.getSelection()
        if (sel.getRangeAt && sel.rangeCount) {
          this.selectedRange = sel.getRangeAt(0)
        }
      } else if (document.selection) {
        this.selectedRange = document.selection.createRange()
      }
    },
    surroundSelection () {
      const span = document.createElement('span')
      span.className = 'highlight'
      const spanId = this.selectedId + ' span-' + this.spanNum
      span.setAttribute('id', spanId)
      span.style.backgroundColor = '#D05555'
      this.$emit('addedSpan', spanId)
      this.spanNum += 1
      if (window.getSelection) {
        var sel = window.getSelection()
        if (sel.rangeCount) {
          var range = this.selectedRange.cloneRange()
          range.surroundContents(span)
          sel.removeAllRanges()
          sel.addRange(range)
        }
      }
    },
    highlight () {
      this.getSelectedRange()
      if (this.selectedRange) {
        this.surroundSelection()
        this.$emit('textHighlighted')
      }
    }
  }
  // watch: {
  //   highlightAllow: function () {
  //     if (this.highlightAllow) {
  //       this.highlight()
  //   },
  // }
}
